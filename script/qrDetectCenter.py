import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

lower_white = np.array([0,0,168], np.uint8)
upper_white = np.array([172,111,255], np.uint8)
detect = False
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
