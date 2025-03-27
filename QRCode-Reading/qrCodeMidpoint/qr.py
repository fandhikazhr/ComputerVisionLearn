import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

### Vision White Node

def nothing(x):
    pass

cap = cv2.VideoCapture(1)
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
while (1):
    _, frame = cap.read()
    success, img = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    if settinghsv:
        l_h = cv2.getTrackbarPos("LH", "Tracking")
        l_s = cv2.getTrackbarPos("LS", "Tracking")
        l_v = cv2.getTrackbarPos("LV", "Tracking")

        u_h = cv2.getTrackbarPos("UH", "Tracking")
        u_s = cv2.getTrackbarPos("US", "Tracking")
        u_v = cv2.getTrackbarPos("UV", "Tracking")

        lower_white = np.array([l_h, l_s, l_v])
        upper_white = np.array([u_h, u_s, u_v])

    else:
        lower_white = np.array([40,0,220], np.uint8)
        upper_white = np.array([179, 255, 255], np.uint8)
        white= cv2.inRange(hsv, lower_white, upper_white)

    mask = cv2.inRange(hsv, lower_white, upper_white)
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

        for c in cnts:
        area = cv2.contourArea(c)
        if(area>5000):
            cv2.drawContours (frame, [c], -1, (0,255,0), 3)
            print ("[INFO], WHITE Detected!")

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
            cv2.putText(frame, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            print("POS X = ", cx,)
            print("POS Y = ", cy,)

        for barcode in decode(img):
            # print(barcode.data)
            myData = barcode.data.decode('utf-8')
            print(myData)
            pts = np.array([barcode.polygon],np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img,[pts],True,(80,255,0),5)
            pts2 = barcode.rect
            cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                        0.9,(80,255,0),3)

        cv2.imshow('QR Analyze', img)
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows() 
