// Function to handle video input change
function handleVideoInput(event) {
    const file = event.target.files[0];
    const videoPlayer = document.getElementById('videoPlayer');
    videoPlayer.src = URL.createObjectURL(file);
    videoPlayer.load();
  
    // Run object detection when video metadata is loaded
    videoPlayer.onloadedmetadata = () => {
      runObjectDetection(videoPlayer);
    };
  }
  
  // Function to run object detection on each video frame
  async function runObjectDetection(videoPlayer) {
    const canvas = document.getElementById('canvas');
    const context = canvas.getContext('2d');
    
    // WebSocket connection to communicate with the backend
    const socket = new WebSocket('ws://localhost:8000');
  
    socket.onopen = () => {
      socket.send('Start'); // Send a message to start object detection
    };
  
    socket.onmessage = (event) => {
      const predictions = JSON.parse(event.data);
      drawBoundingBoxes(predictions);
    };
  
    function drawBoundingBoxes(predictions) {
      context.drawImage(videoPlayer, 0, 0, canvas.width, canvas.height);
  
      // Iterate over the predictions and draw bounding boxes on the canvas
      for (const prediction of predictions) {
        const [x, y, w, h] = prediction.box;
        const label = prediction.label;
        
        context.beginPath();
        context.rect(x, y, w, h);
        context.lineWidth = 2;
        context.strokeStyle = 'red';
        context.fillStyle = 'red';
        context.stroke();
        context.fillText(label, x, y - 10);
      }
    }
  }
  
  // Event listener for video input change
  document.getElementById('videoInput').addEventListener('change', handleVideoInput);
  