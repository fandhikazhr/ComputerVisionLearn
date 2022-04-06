import cv2
import numpy as np
import imutils

lower_blue = np.array([100, 100, 100], np.uint8) # setting the blue lower limit
upper_blue = np.array([125, 255, 255], np.uint8) # setting the blue upper limit
lower_green = np.array([42, 82, 72], np.uint8)  # setting the green lower limit
upper_green = np.array([68, 255, 255], np.uint8)  # setting the green upper limit
lower_red = np.array([0, 90, 70], np.uint8) # setting the red lower limit
upper_red = np.array([10, 255, 255], np.uint8) # setting the re upper limit

cap = cv2.VideoCapture(0)
cap.set(3, 630)
cap.set(4, 360)

while True:
    success, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    blue = cv2.inRange(hsv, lower_blue, upper_blue)
    cnts1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours1 = imutils.grab_contours(cnts1)

    for blueCountour in countours1:
        area1 = cv2.contourArea(blueCountour)
        if (area1 > 5000):
            cv2.drawContours(frame, [blueCountour], -1, (0, 255, 0), 3)
            M = cv2.moments(blueCountour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(M)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

    green = cv2.inRange(hsv, lower_green, upper_green)
    cnts2 = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours2 = imutils.grab_contours(cnts2)

    for greenCountour in countours2:
        area = cv2.contourArea(greenCountour)
        if (area > 5000):
            cv2.drawContours(frame, [greenCountour], -1, (0, 255, 0), 3)
            M = cv2.moments(greenCountour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            
