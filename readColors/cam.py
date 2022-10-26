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
