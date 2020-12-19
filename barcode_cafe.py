import cv2
import numpy as np 
from pyzbar.pyzbar import decode
color = (250,0,10)
colort = (25,0,10)
dic = {}

def resize(img, wi):
    he = int(wi * img.shape[0] / img.shape[1])
    return cv2.resize(img,(wi,he))

def detectBarcode(img, wait):
    
    code = decode(img)
    
    for barCode in code:
        # get message
        text = barCode.data.decode('utf-8')
        print(text)
        dic[text] = ''

        #get index of code and highlight 
        pts = np.array([barCode.polygon], np.int32)
        pts = pts.reshape(-1,1,2)
        cv2.polylines(img, [pts], True, color, 4)

        #show text on code
        pts2 = barCode.rect
        cv2.putText(img, text, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        #show frame image
    cv2.imshow('Result',img)
    if not wait: wait = 0
    cv2.waitKey(wait)

def detectOnVideo(filename):
    if not filename: filename = '0'
    cap = cv2.VideoCapture(filename)
    while True:
        success, img = cap.read()
        if success:
            img = resize(img,1300)
            detectBarcode(img, 10)
        else:
            break
    cap.release()
    cv2.destroyAllWindows()


img = cv2.imread("image/Untitled.png")
# img = resize(img, 1000)

detectBarcode(img, 5 * 1000)
# detectOnVideo('video/athome3.mp4')
print(dic)




