# Tkinter Photo Booth with Face Detection

## Overview

This project creates a simple photo booth application using Python, OpenCV, and Tkinter. The application captures video from the default camera and allows the user to toggle face detection on and off. Users can also take snapshots, which are saved with a unique filename based on the current timestamp.

## Features

- Real-time video feed from the default camera
- Toggleable face detection using Haar cascades
- Ability to take snapshots and save them with a unique timestamp
- User-friendly GUI built with Tkinter

## Requirements

- Python 3.x
- OpenCV
- Tkinter
- PIL (Pillow)

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required Python packages using pip:

    ```bash
    pip install opencv-python-headless pillow
    ```

3. Download the Haar cascade file for face detection from the OpenCV repository: [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml)

4. Save the Haar cascade file in the same directory as your script.

## Usage

1. Save the provided code in a Python script file (e.g., `photo_booth.py`).
2. Ensure the Haar cascade file (`haarcascade_frontalface_default.xml`) and the icon file (`camera_icon.ico`) are in the same directory as the script.
3. Run the script using Python:

    ```bash
    python photo_booth.py
    ```

4. The GUI window will open with the video feed from your default camera.
5. Use the "Toggle Face Detection" button to enable or disable face detection.
6. Use the "Click to take snapshot" button to capture and save a snapshot. The saved images will have filenames based on the current timestamp.

## Code Explanation

### Global Variables

- `show_face_detection`: A boolean variable to toggle face detection on/off.

### Functions

- `toggleFaceDetection()`: Toggles the `show_face_detection` variable to enable or disable face detection.
- `takePic()`: Captures a snapshot of the current video frame, converts it to RGB format, and saves it with a filename based on the current timestamp.
- `faceDetection(frame)`: Detects faces in the given frame and draws rectangles around them if face detection is enabled.

### Main Script

1. Set up the main Tkinter window and configure its properties.
2. Create a label frame (`f1`) to display the video feed.
3. Create buttons for toggling face detection and taking snapshots.
4. Enter a loop to continuously read frames from the video feed, apply face detection (if enabled), and update the video feed in the Tkinter window.
5. Break the loop and close the application if the 'q' key is pressed.
