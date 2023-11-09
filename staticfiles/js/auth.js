const video = document.getElementById('video');
const captureBtn = document.getElementById('capture-btn');

// Check for browser support
if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
  // Access the webcam
  navigator.mediaDevices.getUserMedia({ video: true })
    .then(function(stream) {
      // Display the video stream on the video element
      video.srcObject = stream;
    })
    .catch(function(error) {
      console.error('Error accessing the webcam:', error);
    });
}

// Capture photo from video stream
captureBtn.addEventListener('click', function() {
  const canvas = document.createElement('canvas');
  const context = canvas.getContext('2d');
  canvas.width = video.videoWidth;
  canvas.height = video.videoHeight;
  context.drawImage(video, 0, 0, canvas.width, canvas.height);

  // Convert captured image to Blob
  canvas.toBlob(function(blob) {
    // Create FormData object and append the captured image
    const formData = new FormData();
    formData.append('file', blob, 'photo.jpg');

    // Send the captured image to the API for prediction
    fetch('https://emo-dect-img.onrender.com/predict_emotion', {
      method: 'POST',
      body: formData
    })
    .then(function(response) {
      return response.json();
    })
    .then(function(data) {
      // Check the predicted emotion
      const emotion = data.emotion;
      if (emotion === 'fear' || emotion === 'sad' ) {
        // Redirect to webpage for fear expression
        console.log("Sad or Fear")
        window.location.href = './sorry.html';
      } else {
        // Redirect to webpage for other expressions
        console.log("Happy or Positive")
        window.location.href = './vote.html';
      }
    })
    .catch(function(error) {
      console.error('Error predicting facial expression:', error);
    });
  }, 'image/jpeg');
});
