import cv2
import hand_track_module as htm
from colors import *


###############################
wCam, hCam = 920, 720
###############################


cap = cv2.VideoCapture(cv2.CAP_DSHOW,0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) !=0:
        x1, y1 = lmList[12][1], lmList[12][2]
        x2, y2 = lmList[0][1], lmList[0][2]
        cx, cy = (x1+x2) // 2, (y1+y2) // 2

        cv2.circle(img, (cx, cy), 200, white, cv2.FILLED)
        cv2.circle(img, (cx, cy), 150, red, cv2.FILLED)
        cv2.circle(img, (cx, cy), 100, lite_blue, cv2.FILLED)

    cv2.imshow("Captain", img)

    if cv2.waitKey(1) == ord('q'):
        break