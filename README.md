# Webcam Frame Capture and Recording

This project is designed to capture frames from a webcam and record video using a web application. It consists of a Flask backend that processes the captured frames and a frontend that captures the frames from the webcam.

## Features

- **Frame Capture**: Captures frames from the webcam at a specified frame rate.
- **Video Recording**: Records video from the webcam and sends the recorded chunks to the backend.
- **Backend Processing**: Processes the captured frames and video chunks, saving them as images and video files.

## Prerequisites

- Python 3.x
- Flask
- OpenCV
- Redis
- RQ (Redis Queue)

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/cam2bytes.git
   ```
2. Navigate to the project directory:
   ```
   cd cam2bytes
   ```
3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
4. Start the Redis server (if not already running):
   ```
   redis-server
   ```
5. Start the Redis worker :
   ```
   rq worker
   ```
6. Run the Flask application:
   ```
   python app.py
   ```
7. OPTIONAL: Monitor tasks on the Redis dashboard:
   ```
   rq dashboard
   ```

## Usage

1. Open a web browser and navigate to `http://127.0.0.1:5000/`.
2. Click on the "Start Capture" button to start capturing frames from the webcam.
3. Click on the "Stop Capture" button to stop capturing frames.

For video recording, navigate to `http://127.0.0.1:5000/mediarec.html` and follow the instructions on the page.

## Backend

The backend is built with Flask and uses Redis and RQ for task queueing. The `process_url` function in `tasks.py` processes the captured frames and video chunks, converting them from base64 data URLs to images and video files.

## Frontend

The frontend is a simple HTML page with JavaScript for capturing frames from the webcam and recording video. It uses the `navigator.mediaDevices.getUserMedia` API for accessing the webcam and the `MediaRecorder` API for recording video.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.
