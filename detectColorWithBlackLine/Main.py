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
