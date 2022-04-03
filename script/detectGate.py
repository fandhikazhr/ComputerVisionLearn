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

    for c in cnts:
        area = cv2.contourArea(c)
        if(area>5000):
            cv2.drawContours (frame, [c], -1, (0,255,0), 3)
            print ("[INFO], Red Detected!")

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            print("POS X = ", cx,)
            print("POS Y = ", cy,)
    ims= cv2.resize(mask, (640,360))
