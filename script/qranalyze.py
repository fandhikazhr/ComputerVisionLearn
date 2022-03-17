import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

lower_white = np.array([40,0,220], np.uint8)
upper_white = np.array([172,255,255], np.uint8)
lower_black = np.uint8([5,5,5])
upper_black = np.uint8([0,0,0])

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
