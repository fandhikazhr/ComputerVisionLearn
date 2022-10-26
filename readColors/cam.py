import cv2
import numpy as np
import imutils

def stackImages(scale, imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range(0,rows):
            for y in range(0,cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0,0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0,0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor = np.hstack(imgArray)
        ver = hor
    return ver

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

settinghsv=True
settinghsv2=True

if settinghsv:
    cv2.namedWindow("Line Tracking")
    cv2.createTrackbar("LH", "Line Tracking", 0, 255, nothing)
    cv2.createTrackbar("LS", "Line Tracking", 0, 255, nothing)
    cv2.createTrackbar("LV", "Line Tracking", 205, 255, nothing)
    cv2.createTrackbar("UH", "Line Tracking", 179, 255, nothing)
    cv2.createTrackbar("US", "Line Tracking", 255, 255, nothing)
    cv2.createTrackbar("UV", "Line Tracking", 255, 255, nothing)

if settinghsv2:
    cv2.namedWindow("Red Gate")
    cv2.createTrackbar("LH", "Red Gate", 0, 255, nothing)
    cv2.createTrackbar("LS", "Red Gate", 70, 255, nothing)
    cv2.createTrackbar("LV", "Red Gate", 50, 255, nothing)
    cv2.createTrackbar("UH", "Red Gate", 10, 255, nothing)
    cv2.createTrackbar("US", "Red Gate", 255, 255, nothing)
    cv2.createTrackbar("UV", "Red Gate", 255, 255, nothing)

while (1):
    
    _, frame = cap.read()
    _, frame2 = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

    if settinghsv:
        l_h = cv2.getTrackbarPos("LH", "Line Tracking")
        l_s = cv2.getTrackbarPos("LS", "Line Tracking")
        l_v = cv2.getTrackbarPos("LV", "Line Tracking")

        u_h = cv2.getTrackbarPos("UH", "Line Tracking")
        u_s = cv2.getTrackbarPos("US", "Line Tracking")
        u_v = cv2.getTrackbarPos("UV", "Line Tracking")

        lower_white = np.array([l_h, l_s, l_v])
        upper_white = np.array([u_h, u_s, u_v])

    if settinghsv2:
        l_h = cv2.getTrackbarPos("LH", "Red Gate")
        l_s = cv2.getTrackbarPos("LS", "Red Gate")
        l_v = cv2.getTrackbarPos("LV", "Red Gate")

        u_h = cv2.getTrackbarPos("UH", "Red Gate")
        u_s = cv2.getTrackbarPos("US", "Red Gate")
        u_v = cv2.getTrackbarPos("UV", "Red Gate")

        lower_red = np.array([l_h, l_s, l_v])
        upper_red = np.array([u_h, u_s, u_v])
        
    mask = cv2.inRange(hsv, lower_white, upper_white)
    cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for b in cnts:
        area = cv2.contourArea(b)
        if(area>5000):
            cv2.drawContours (frame, [b], -1, (0,255,0), 3)
            print ("[INFO], WHITE Detected!")

            M = cv2.moments(b)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
            # cv2.putText(frame, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            # cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # print("POS X = ", cx,)
            # print("POS Y = ", cy,)

    mask2 = cv2.inRange(hsv2, lower_red, upper_red)
    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    for c in cnts2:
        area = cv2.contourArea(c)
        if(area>5000):
            cv2.drawContours (frame2, [c], -1, (0,255,0), 3)
            # print ("[INFO], Red Detected!")

            M = cv2.moments(c)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame2, (cx,cy),7,(255,255,255),-1)
            # cv2.putText(frame2, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            # cv2.putText(frame2,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # cv2.putText(frame2,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # print("POS X = ", cx,)
            # print("POS Y = ", cy,)

    imgResult = stackImages(0.6,([frame,mask])) 
    cv2.imshow("Results", imgResult)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
