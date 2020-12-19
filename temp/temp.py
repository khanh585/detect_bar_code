import cv2
import numpy as np
import imutils

kernel = np.ones((5,5), np.uint8)


def func(img):
    imgGRAY = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    imgBlur = cv2.GaussianBlur(imgGRAY, (15,15),0)

    imgCanny = cv2.Canny(imgBlur, 10,20)
    # cv2.imshow('imgCanny',imgCanny)

    imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
    # cv2.imshow('imgDialation',imgDialation)

    # imgEroded = cv2.erode(imgDialation, kernel, iterations=1)
    # cv2.imshow('imgEroded',imgEroded)
    kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 10))
    closed = cv2.morphologyEx(imgDialation, cv2.MORPH_CLOSE, kernel)

    # perform a series of erosions and dilations
    closed = cv2.erode(closed, None, iterations = 5)
    closed = cv2.dilate(closed, None, iterations = 9)
    
    # cv2.imshow('closed',closed)

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
        cv2.drawContours(img, [box], -1, (0, 255, 0), 3)
        cv2.putText(img, 'Ky', (box[0][0],box[0][1]), cv2.LINE_AA, 2, (220,0,0), 2)

    cv2.imshow('Image', img)


# resize
# wi = 600
# he = int(wi * img.shape[0] / img.shape[1])

# imgResize = cv2.resize(img,(wi,he))
# imgCrop = img[0:he,0:wi]

# cv2.imshow('Image', img)
# cv2.imshow('imgResize', imgResize)
# cv2.imshow('imgCrop', imgCrop)


cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    func(img)
    cv2.waitKey(1)