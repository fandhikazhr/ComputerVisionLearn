import cv2
import numpy as np
import imutils
from pyzbar.pyzbar import decode

lower_white = np.array([0,0,168], np.uint8)
upper_white = np.array([172,111,255], np.uint8)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

while True:
    success, img = cap.read()
    for barcode in decode(img):
        myData = barcode.data.decode('utf-8')
        # print(myData)
        # print(barcode)
        # center = cv2.moments(barcode)
        # cx = int(center["m10"] / center["m00"])
        # cy = int(center["m01"] / center["m00"])
        pts = np.array([barcode.polygon],np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(img,[pts],True,(80,255,0),5)
        pts2 = barcode.rect
        # cx = int((pts2[0]/2) * (pts2[2]/2))
        # cy = int((pts2[1]/2) * (pts2[3]/2))
        # print(cx)
        # print(cy)
        # M = cv2.moments(pts2)
        # cx = int(M["m10"] / M["m01"])
        # cy = int(M["m03"] / M["m00"])
        # print(M)
        # cv2.circle(img, (cx,cy), 10, (0,0,255), -1)
        cv2.putText(img,myData,(pts2[0],pts2[1]),cv2.FONT_HERSHEY_SIMPLEX,
                    0.9,(80,255,0),3)
   
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    white = cv2.inRange(hsv, lower_white, upper_white)
    cnts1 = cv2.findContours(white, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours1 = imutils.grab_contours(cnts1)
    
    for whiteCountour in countours1:
        area = cv2.contourArea(whiteCountour)
        if(area > 5000):
            M = cv2.moments(whiteCountour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(M)
            cv2.circle(img, (cx, cy), 7, (0, 0, 255), -1)
    cv2.imshow('white',white)
    cv2.imshow('Output', img)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()
