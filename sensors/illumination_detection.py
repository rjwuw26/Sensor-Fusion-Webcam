"""
Author: Ryan Wilkerson
Version: 10/29/2025
Desc: A simple illumination detection sensor using OpenCV.
This script captures video from the webcam, calculates the average brightness of each frame 
and displays it on the video feed.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    brightness = np.mean(gray)

    cv2.putText(frame, f'Brightness: {brightness:.2f}', (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
    cv2.imshow('Illumination Sensor', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
