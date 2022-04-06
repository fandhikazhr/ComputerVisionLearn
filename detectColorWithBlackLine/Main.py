import cv2
import numpy as np
import imutils

def nothing(x):
    pass

lower_blue = np.array([100, 100, 100], np.uint8) # setting the blue lower limit
upper_blue = np.array([125, 255, 255], np.uint8) # setting the blue upper limit
lower_green = np.array([42, 82, 72], np.uint8)  # setting the green lower limit
upper_green = np.array([68, 255, 255], np.uint8)  # setting the green upper limit
lower_red = np.array([0, 90, 70], np.uint8) # setting the red lower limit
upper_red = np.array([10, 255, 255], np.uint8) # setting the re upper limit

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

cap.set(3, 630)
cap.set(4, 360)

print ("QR Detection Starting...")
while True:
    success, frame = cap.read()
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
    
    blue = cv2.inRange(hsv, lower_blue, upper_blue)
    cnts1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours1 = imutils.grab_contours(cnts1)

    for blueCountour in countours1:
        area1 = cv2.contourArea(blueCountour)
        if (area1 > 5000):
            cv2.drawContours(frame, [blueCountour], -1, (0, 255, 0), 3)
            M = cv2.moments(blueCountour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            print(M)
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

    green = cv2.inRange(hsv, lower_green, upper_green)
    cnts2 = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours2 = imutils.grab_contours(cnts2)
    
    for greenCountour in countours2:
        area = cv2.contourArea(greenCountour)
        if (area > 5000):
            cv2.drawContours(frame, [greenCountour], -1, (0, 255, 0), 3)
            M = cv2.moments(greenCountour)
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            
    red = cv2.inRange(hsv, lower_red, upper_red)
    cnts3 = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    countours3 = imutils.grab_contours(cnts3)

    for redCountour in countours3:
        area = cv2.contourArea(redCountour)
        if (area > 5000):
            cv2.drawContours(frame, [redCountour], -1, (0, 255, 0), 3)

            M = cv2.moments(redCountour)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)

    k = cv2.waitKey(5)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
