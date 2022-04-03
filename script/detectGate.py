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
while (1):
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if settinghsv:
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        lower_red = np.array([l_h, l_s, l_v])
        upper_red = np.array([u_h, u_s, u_v])

    else:
        lower_red = np.array([0, 70, 50], np.uint8)
        upper_red = np.array([10, 255, 255], np.uint8)
        red = cv2.inRange(hsv, lower_red, upper_red)

    mask = cv2.inRange(hsv, lower_red, upper_red)
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
