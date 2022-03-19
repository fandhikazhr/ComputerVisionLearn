import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

### Vision White Node

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
settinghsv=True
if settinghsv:
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 40, 100, nothing)
    cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 220, 255, nothing)
    cv2.createTrackbar("UH", "Tracking", 179, 255, nothing)
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
print ("QR Detection Starting...")
