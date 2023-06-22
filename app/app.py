from flask import Flask, render_template, request, redirect, url_for, Response
import os
import cv2
import torch
from PIL import Image
from torchvision.transforms import functional as F
from film-sight import detect

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True).to(device).eval()

def detect_objects(frame):
    # Convert frame to PIL Image
    image = Image.fromarray(frame)

    # Preprocess image
    image = F.to_tensor(image).unsqueeze(0).to(device)

    # Run object detection
    results = model(image)

    # Get bounding box coordinates and labels
    boxes = results.xyxy[0].cpu().numpy()
    labels = results.names[results.pred[0].cpu()]

    # Draw bounding boxes and labels on the frame
    for box, label in zip(boxes, labels):
        xmin, ymin, xmax, ymax, _ = box
        cv2.rectangle(frame, (int(xmin), int(ymin)), (int(xmax), int(ymax)), (0, 255, 0), 2)
        cv2.putText(frame, label, (int(xmin), int(ymin) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    return frame

def video_feed(video_path):
    video = cv2.VideoCapture(video_path)

    while True:
        ret, frame = video.read()

        if not ret:
            break

        frame = cv2.resize(frame, (640, 480))
        frame = detect_objects(frame)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    video.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(url_for('index'))

    file = request.files['file']
    if file.filename == '':
        return redirect(url_for('index'))

    video_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(video_path)

    return redirect(url_for('video', video_path=video_path))

@app.route('/video/<video_path>')
def video(video_path):
    return Response(video_feed(video_path),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
