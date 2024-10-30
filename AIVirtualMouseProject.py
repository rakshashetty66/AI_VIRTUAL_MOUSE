import cv2
import numpy as np
import HandTrackingModule as htm
import time
import autopy


# Camera and Screen Configuration
wCam, hCam = 1280, 720  # Set camera to a standard resolution
frameR = 10  # Boundary margin for hand tracking frame
smoothening = 4  # Increase for smoother movement, but might slow response slightly

pTime = 0  # For FPS calculation
plocX, plocY = 0, 0  # Previous location for cursor
clocX, clocY = 0, 0  # Current location for cursor

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# Initialize Hand Detector
detector = htm.handDetector(maxHands=1)
wScr, hScr = autopy.screen.size()  # Get screen size

while True:
    # Capture frame-by-frame
    success, img = cap.read()
    img = detector.findHands(img)  # Detect hand
    lmList, bbox = detector.findPosition(img)  # Get landmarks list

    # Check if any landmarks were found
    if lmList:
        # Get coordinates of index and middle fingers
        x1, y1 = lmList[8][1:]  # Index finger tip
        x2, y2 = lmList[12][1:]  # Middle finger tip

        # Check which fingers are up
        fingers = detector.fingersUp()

        # Moving Mode: Only index finger up
        if fingers[1] == 1 and fingers[2] == 0:
            # Convert coordinates for screen
            x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
            y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))

            # Smooth movement
            clocX = plocX + (x3 - plocX) / smoothening
            clocY = plocY + (y3 - plocY) / smoothening

            # Move mouse cursor
            autopy.mouse.move(wScr - clocX, clocY)
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            plocX, plocY = clocX, clocY  # Update previous location

        # Clicking Mode: Both index and middle fingers up
        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = detector.findDistance(8, 12, img)
            if length < 40:  # Threshold distance for click
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()  # Left click

    # Draw boundary for tracking frame
    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    # Calculate Frame Rate
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    # Display FPS on screen
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # Show the image
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == 27:  # Press 'Esc' to exit
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
