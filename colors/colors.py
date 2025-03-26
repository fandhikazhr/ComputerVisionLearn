import cv2
import numpy as np
import imutils

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 100], np.uint8) # setting the blue lower limit
    upper_blue = np.array([120, 255, 255], np.uint8) # setting the blue upper limit
    blue = cv2.inRange(hsv, lower_blue, upper_blue)

    cnts1 = cv2.findContours(blue, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts1 = imutils.grab_contours(cnts1)
    
    for c in cnts1:
        area = cv2.contourArea(c)
        if (area > 5000):
            cv2.drawContours(frame, [c], -1, (0, 255, 0), 3)

            M = cv2.moments(c)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Centre", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            print("area ", area)
            print("the coordinate is..", cx, cy)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(5)
        if k == 27:
        break
    # 30, 82, 72
    # 102, 255, 255
    lower_green = np.array([30, 82, 72], np.uint8)  # setting the green lower limit
    upper_green = np.array([102, 255, 255], np.uint8)  # setting the green upper limit
    green = cv2.inRange(hsv, lower_green, upper_green)

    cnts2 = cv2.findContours(green, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts2 = imutils.grab_contours(cnts2)

    for g in cnts2:
        area = cv2.contourArea(g)
        if (area > 5000):
            cv2.drawContours(frame, [g], -1, (0, 255, 0), 3)

            M = cv2.moments(g)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Centre", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            print("area ", area)
            print("the coordinate is..", cx, cy)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(5)
        if k == 27:
            break
    # 0, 50, 50
    # 10, 255, 255
    lower_red = np.array([0, 90, 70], np.uint8) # setting the red lower limit
    upper_red = np.array([67, 255, 255], np.uint8) # setting the re upper limit
    red = cv2.inRange(hsv, lower_red, upper_red)

    cnts3 = cv2.findContours(red, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts3 = imutils.grab_contours(cnts3)

    for r in cnts3:
        area = cv2.contourArea(r)
        if(area > 5000):
            cv2.drawContours(frame, [r], -1, (0, 255, 0), 3)

            M = cv2.moments(r)

            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])

            cv2.circle(frame, (cx, cy), 7, (255, 255, 255), -1)
            cv2.putText(frame, "Centre", (cx - 20, cy - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
            print("area ", area)
            print("the coordinate is..", cx, cy)

        cv2.imshow("frame", frame)

        k = cv2.waitKey(5)
        if k == 27:
            break

cap.release()
cv2.destroyAllWindows()
