import cv2
import numpy as np
import imutils

def nothing(x):
    pass

cap = cv2.VideoCapture(0)
settinghsv=True
if settinghsv:
    cv2.namedWindow("Tracking")
    cv2.createTrackbar("LH", "Tracking", 0, 255, nothing)
    cv2.createTrackbar("LS", "Tracking", 70, 255, nothing)
    cv2.createTrackbar("LV", "Tracking", 50, 255, nothing)
    cv2.createTrackbar("UH", "Tracking", 10, 255, nothing)
    cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
print ("QR Detection Starting...")
