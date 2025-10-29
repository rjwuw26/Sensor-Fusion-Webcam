"""
Author: Ryan Wilkerson
Version: 10/29/2025
Desc: A simple motion detection sensor using OpenCV.
This script captures video from the webcam, detects motion by comparing consecutive frames, 
and displays the motion state on the video feed.
"""

import cv2

cap = cv2.VideoCapture(0)
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)
motion_history = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    diff = cv2.absdiff(prev_gray, gray)
    _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
    motion_score = cv2.countNonZero(thresh)

    motion_history.append(motion_score)
    if len(motion_history) > 5:
        motion_history.pop(0)
    
    avg_motion = sum(motion_history) / len(motion_history)

    if avg_motion > 1000:
        motion_state = "Motion Detected"
    else:
        motion_state = "No Motion"

    cv2.putText(frame, f'State: {motion_state}', (10, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        
    cv2.imshow('Webcam Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    prev_gray = gray.copy()

cap.release()
cv2.destroyAllWindows()