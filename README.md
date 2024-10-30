# AI Virtual Mouse Using Hand Gestures
This Python project demonstrates an AI-powered virtual mouse that uses hand gestures to control cursor movement and perform click actions. It leverages OpenCV for image processing, MediaPipe for hand tracking, and AutoPy for controlling the mouse on the screen.

# Features
1. Cursor Control: Uses hand gestures to move the cursor on the screen.
2. Click Actions: Recognizes index and middle finger gestures to perform left-click actions.
3. Smooth Movement: Includes a smoothing algorithm for fluid cursor movement.
4. FPS Display: Displays the real-time frame rate on the screen.

# Libraries Used
1. OpenCV: For image processing and displaying webcam feed.
2. MediaPipe: For hand landmark detection and tracking.
3. AutoPy: For controlling the mouse cursor and executing click events.
4. NumPy: For efficient mathematical calculations.

# Code Overview

handDetector Class
1. Initializes and configures the MediaPipe hand model.
2. Includes methods to:
a) Detect hands and draw landmarks.
b) Track hand position and determine finger states (up or down).
c) Calculate the distance between fingers for recognizing gestures.

# Main Loop
1. Capture Webcam Feed: Reads frames from the webcam and processes them in real time.
2. Hand Detection: Detects hand landmarks and calculates the positions of the index and middle fingers.
3. Cursor Movement Mode: Moves the cursor based on the index finger's position.
4. Click Mode: Checks the distance between index and middle fingers to perform a left-click.
5. Display FPS: Calculates and displays frames per second on the screen for performance monitoring.

# File Structure
1. AiVirtualMouseProject.py: Main file to execute the virtual mouse.
2. HandTrackingModule.py: Contains the handDetector class for hand tracking and gesture recognition.

# Customization
1. Screen and Camera Configuration: Modify wCam, hCam, wScr, hScr for custom camera and screen resolutions.
2. Sensitivity and Smoothing: Adjust smoothening for faster or smoother cursor movement.
3. Gesture Thresholds: Modify click threshold distance and finger states for additional gestures or fine-tuning.
4. This project enables touchless interaction with your computer using simple hand gestures, making it a fun and interactive AI-based application.






