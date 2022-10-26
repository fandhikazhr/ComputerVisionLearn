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

# lower_blue = np.array([100, 100, 100], np.uint8) # setting the blue lower limit
# upper_blue = np.array([125, 255, 255], np.uint8) # setting the blue upper limit
# lower_green = np.array([42, 82, 72], np.uint8)  # setting the green lower limit
# upper_green = np.array([68, 255, 255], np.uint8)  # setting the green upper limit
# lower_red = np.array([0, 90, 70], np.uint8) # setting the red lower limit
# upper_red = np.array([10, 255, 255], np.uint8) # setting the re upper limit
#
# cap = cv2.VideoCapture(0)
# cap.set(3, 630)
# cap.set(4, 360)
#
# while True:
#     success, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     blue = cv2.inRange(hsv, lower_blue, upper_blue)
#     cnts1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     countours1 = imutils.grab_contours(cnts1)
#
#     for blueCountour in countours1:
#         area1 = cv2.contourArea(blueCountour)
#         if (area1 > 5000):
#             cv2.drawContours(frame, [blueCountour], -1, (0, 255, 0), 3)
#             M = cv2.moments(blueCountour)
#             cx = int(M["m10"] / M["m00"])
#             cy = int(M["m01"] / M["m00"])
#             print(M)
#             cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
#
#     green = cv2.inRange(hsv, lower_green, upper_green)
#     cnts2 = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     countours2 = imutils.grab_contours(cnts2)
#
#     for greenCountour in countours2:
#         area = cv2.contourArea(greenCountour)
#         if (area > 5000):
#             cv2.drawContours(frame, [greenCountour], -1, (0, 255, 0), 3)
#             M = cv2.moments(greenCountour)
#             cx = int(M["m10"] / M["m00"])
#             cy = int(M["m01"] / M["m00"])
#             cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
#
#     red = cv2.inRange(hsv, lower_red, upper_red)
#     cnts3 = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     countours3 = imutils.grab_contours(cnts3)
#
#     for redCountour in countours3:
#         area = cv2.contourArea(redCountour)
#         if (area > 5000):
#             cv2.drawContours(frame, [redCountour], -1, (0, 255, 0), 3)
#
#             M = cv2.moments(redCountour)
#
#             cx = int(M["m10"] / M["m00"])
#             cy = int(M["m01"] / M["m00"])
#
#             cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
#
#     cv2.imshow("frame", frame)
#
#     k = cv2.waitKey(5)
#     if k == 27:
#         break

## Optional Code (You can use this on for loop)
 # cv2.putText(frame, "Centre", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
 # print("area ", area)
 # print("the coordinate is..", cx, cy)

# cap.release()
# cv2.destroyAllWindows()

### Vision White Node

# def nothing(x):
#     pass
#
# cap = cv2.VideoCapture(1)
# settinghsv=True
# if settinghsv:
#     cv2.namedWindow("Tracking")
#     cv2.createTrackbar("LH", "Tracking", 40, 100, nothing)
#     cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
#     cv2.createTrackbar("LV", "Tracking", 220, 255, nothing)
#     cv2.createTrackbar("UH", "Tracking", 179, 255, nothing)
#     cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
#     cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)
# print ("QR Detection Starting...")
# while (1):
#     _, frame = cap.read()
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#     if settinghsv:
#         l_h = cv2.getTrackbarPos("LH", "Tracking")
#         l_s = cv2.getTrackbarPos("LS", "Tracking")
#         l_v = cv2.getTrackbarPos("LV", "Tracking")
#
#         u_h = cv2.getTrackbarPos("UH", "Tracking")
#         u_s = cv2.getTrackbarPos("US", "Tracking")
#         u_v = cv2.getTrackbarPos("UV", "Tracking")
#
#         lower_white = np.array([l_h, l_s, l_v])
#         upper_white = np.array([u_h, u_s, u_v])
#
#     else:
#         lower_white = np.array([40,0,220], np.uint8)
#         upper_white = np.array([179, 255, 255], np.uint8)
#         white= cv2.inRange(hsv, lower_white, upper_white)
#
#     mask = cv2.inRange(hsv, lower_white, upper_white)
#     cnts = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = imutils.grab_contours(cnts)
#
#     for c in cnts:
#         area = cv2.contourArea(c)
#         if(area>5000):
#             cv2.drawContours (frame, [c], -1, (0,255,0), 3)
#             print ("[INFO], WHITE Detected!")
#
#             M = cv2.moments(c)
#
#             cx = int(M["m10"]/M["m00"])
#             cy = int(M["m01"]/M["m00"])
#             cv2.circle(frame, (cx,cy),7,(255,255,255),-1)
#             cv2.putText(frame, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
#             cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
#             cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
#             print("POS X = ", cx,)
#             print("POS Y = ", cy,)
#
#     cv2.imshow("frame", frame)
#     cv2.imshow("mask", mask)
#
#     key = cv2.waitKey(1)
#     if key == 27:
#         break
#
# cap.release()
# cv2.destroyAllWindows()


### Vision Red Node

def nothing(x):
    pass

cap = cv2.VideoCapture(0)

# if settinghsv:
cv2.namedWindow("Tracking Red")
cv2.createTrackbar("LH", "Tracking Red", 0, 255, nothing)
cv2.createTrackbar("LS", "Tracking Red", 90, 255, nothing)
cv2.createTrackbar("LV", "Tracking Red", 70, 255, nothing)
cv2.createTrackbar("UH", "Tracking Red", 10, 255, nothing)
cv2.createTrackbar("US", "Tracking Red", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking Red", 255, 255, nothing)

cv2.namedWindow("Tracking Green")
cv2.createTrackbar("LH", "Tracking Green", 42, 255, nothing)
cv2.createTrackbar("LS", "Tracking Green", 82, 255, nothing)
cv2.createTrackbar("LV", "Tracking Green", 72, 255, nothing)
cv2.createTrackbar("UH", "Tracking Green", 97, 255, nothing)
cv2.createTrackbar("US", "Tracking Green", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking Green", 255, 255, nothing)

cv2.namedWindow("Tracking Blue")
cv2.createTrackbar("LH", "Tracking Blue", 100, 255, nothing)
cv2.createTrackbar("LS", "Tracking Blue", 100, 255, nothing)
cv2.createTrackbar("LV", "Tracking Blue", 100, 255, nothing)
cv2.createTrackbar("UH", "Tracking Blue", 125, 255, nothing)
cv2.createTrackbar("US", "Tracking Blue", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking Blue", 255, 255, nothing)

while (1):
    #frame = cv2.imread('smarties.png')
    _, frame = cap.read()
    _, frame2 = cap.read()
    _, frame3 = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
    hsv3 = cv2.cvtColor(frame3, cv2.COLOR_BGR2HSV)

    # if settinghsv:
    l_h = cv2.getTrackbarPos("LH", "Tracking Red")
    l_s = cv2.getTrackbarPos("LS", "Tracking Red")
    l_v = cv2.getTrackbarPos("LV", "Tracking Red")

    u_h = cv2.getTrackbarPos("UH", "Tracking Red")
    u_s = cv2.getTrackbarPos("US", "Tracking Red")
    u_v = cv2.getTrackbarPos("UV", "Tracking Red")

    lower_red = np.array([l_h, l_s, l_v])
    upper_red = np.array([u_h, u_s, u_v])

    L_H = cv2.getTrackbarPos("LH", "Tracking Green")
    L_S = cv2.getTrackbarPos("LS", "Tracking Green")
    L_V = cv2.getTrackbarPos("LV", "Tracking Green")

    U_H = cv2.getTrackbarPos("UH", "Tracking Green")
    U_S = cv2.getTrackbarPos("US", "Tracking Green")
    U_V = cv2.getTrackbarPos("UV", "Tracking Green")

    lower_green = np.array([L_H, L_S, L_V])
    upper_green = np.array([U_H, U_S, U_V])

    l_H = cv2.getTrackbarPos("LH", "Tracking Blue")
    l_S = cv2.getTrackbarPos("LS", "Tracking Blue")
    l_V = cv2.getTrackbarPos("LV", "Tracking Blue")

    u_H = cv2.getTrackbarPos("UH", "Tracking Blue")
    u_S = cv2.getTrackbarPos("US", "Tracking Blue")
    u_V = cv2.getTrackbarPos("UV", "Tracking Blue")

    lower_blue = np.array([l_H, l_S, l_V])
    upper_blue = np.array([u_H, u_S, u_V])

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
            # cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # print("POS X = ", cx,)
            # print("POS Y = ", cy,)
    
    mask2 = cv2.inRange(hsv2, lower_green, upper_green)
    cnts2 = cv2.findContours(mask2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    for g in cnts2:
        area = cv2.contourArea(g)
        if(area>5000):
            cv2.drawContours (frame2, [g], -1, (0,255,0), 3)
            print ("[INFO], Green Detected!")

            M = cv2.moments(g)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame2, (cx,cy),7,(255,255,255),-1)
            cv2.putText(frame2, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            # cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # print("POS X = ", cx,)
            # print("POS Y = ", cy,)

    mask3 = cv2.inRange(hsv3, lower_blue, upper_blue)
    cnts3 = cv2.findContours(mask3, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    for b in cnts3:
        area = cv2.contourArea(b)
        if(area>5000):
            cv2.drawContours (frame3, [b], -1, (0,255,0), 3)
            print ("[INFO], Blue Detected!")

            M = cv2.moments(b)

            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            cv2.circle(frame3, (cx,cy),7,(255,255,255),-1)
            cv2.putText(frame3, "Centre", (cx-20, cy-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
            # cv2.putText(frame,"POS X= "+str(cx), (20,29), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # cv2.putText(frame,"POS Y= "+str(cy), (20,60), cv2.FONT_HERSHEY_SIMPLEX,1.0,(0,0,255), 2)
            # print("POS X = ", cx,)
            # print("POS Y = ", cy,)

    imgResult = stackImages(0.4,([frame,mask],[frame2, mask2],[frame3, mask3])) 
    cv2.imshow("Results", imgResult)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

