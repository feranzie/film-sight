from flask import Flask, request, jsonify
import torch
from torchvision.transforms import functional as F
from PIL import Image
from io import BytesIO
import base64
import time

app = Flask(__name__)

# Load the YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# WebSocket endpoint for object detection
@app.route('/detect', methods=['POST'])
def detect():
    video_data = request.files['video'].read()
    video_stream = BytesIO(video_data)
    predictions = []

    # Iterate over video frames and perform object detection
    for frame_data in get_video_frames(video_stream):
        frame = Image.open(BytesIO(frame_data)).convert('RGB')
        predictions.append(model(frame))

    return jsonify(predictions)

# Function to extract frames from video stream
def get_video_frames(video_stream):
    video = cv2.VideoCapture(video_stream)
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        yield frame

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
