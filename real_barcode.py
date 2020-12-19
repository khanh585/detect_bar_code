# import the necessary packages
import numpy as np
import argparse
import imutils
import cv2

def detect(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ddepth = cv2.cv.CV_32F if imutils.is_cv2() else cv2.CV_32F
    ddepth = 3
    gradX = cv2.Sobel(gray, ddepth=ddepth, dx=1, dy=0, ksize=0)
    gradY = cv2.Sobel(gray, ddepth=ddepth, dx=0, dy=1, ksize=0)
    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)

    cv2.imshow('gradient',gradient)
    # blur and threshold the image
    blurred = cv2.blur(gradient, (8, 9))
    (_, thresh) = cv2.threshold(blurred, 225, 255, cv2.THRESH_BINARY)
    cv2.imshow('thresh',thresh)
    

    # construct a closing kernel and apply it to the thresholded image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
    closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations = 4)
    closed = cv2.dilate(closed, None, iterations = 4)
    
    cv2.imshow('closed',closed)
    cv2.waitKey(1)

    # find the contours in the thresholded image, then sort the contours
    # by their area, keeping only the largest one
    cnts = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if cnts:
        c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        # compute the rotated bounding box of the largest contour
        rect = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(rect) if imutils.is_cv2() else cv2.boxPoints(rect)
        box = np.int0(box)
        # draw a bounding box arounded the detected barcode and display the
        # image
        cv2.drawContours(image, [box], -1, (0, 255, 0), 3)

# load the image and convert it to grayscale
# img = cv2.imread("image/barcode_01.jpg")
# detect(img)
# cv2.imshow('Result',img)
# cv2.waitKey(0)

cap = cv2.VideoCapture(0)
cap.set(3,240)
cap.set(4,180)


while True:
    success, image = cap.read()
    if(success):
        detect(image)
        cv2.imshow('Result',image)
    cv2.waitKey(1)





