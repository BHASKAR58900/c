import cv2
import time
import math
video=cv2.VideoCapture("bb3.mp4")
tracker=cv2.TrackerCSRT_create()
returned,img=video.read()
bbox=cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)
print(bbox)
while True:
    check,img=video.read()
    cv2.imshow("window",img)
    key=cv2.waitKey(25)
    if key==32:
        print("stopped")
        break
video.release()
cv2.destroyAllWindows()
