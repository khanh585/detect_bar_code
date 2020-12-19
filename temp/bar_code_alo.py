import cv2
import numpy as np 
from pyzbar.pyzbar import decode
color = (250,0,10)
colort = (25,0,10)


img = cv2.imread("i12.png")

# resize
# wi = 500
# he = int(wi * img.shape[0] / img.shape[1])
# img = cv2.resize(img,(wi,he))


code = decode(img)

for barCode in code:
    # get message
    text = barCode.data.decode('utf-8')
    print(text)
    #get index of code and highlight 
    pts = np.array([barCode.polygon], np.int32)
    pts = pts.reshape(-1,1,2)
    cv2.polylines(img, [pts], True, color, 4)

    #show text on code
    pts2 = barCode.rect
    cv2.putText(img, text, (pts2[0],pts2[2]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    #show frame image
cv2.imshow('Result',img)
cv2.waitKey(0)

# cap = cv2.VideoCapture("0")


# while True:
#     success, img = cap.read()
#     if success:
#         code = decode(img)
#         for barCode in code:
#             # get message
#             text = barCode.data.decode('utf-8')
#             #get index of code and highlight 
#             pts = np.array([barCode.polygon], np.int32)
#             pts = pts.reshape(-1,1,2)
#             cv2.polylines(img, [pts], True, color, 4)

#             #show text on code
#             pts2 = barCode.rect
#             cv2.putText(img, text, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.6, colort, 2)

#         #show frame image
#         cv2.imshow('Result',img)
#         cv2.waitKey(1)
#     else:
#         break
# cap.release()
# cv2.destroyAllWindows()

