import cv2
import hand_track_module as htm
from colors import *


###############################
wCam, hCam = 640, 480
###############################


cap = cv2.VideoCapture('http://192.168.43.228:8080/video')
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7)


while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) !=0:
        x1, y1 = lmList[9][1], lmList[9][2]
        x2, y2 = lmList[0][1], lmList[0][2]
        cx, cy = (x1+x2) // 2, (y1+y2) // 2

        # cv2.line(img, (x1, y1), (x2, y2), (255,255,0), 4) 
        # cv2.circle(img, (x1, y2), 150, (255, 255, 255), cv2.FILLED)
        # cv2.circle(img, (x2, y2), 100, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 36, black, 4)
        cv2.circle(img, (cx, cy), 35, black, cv2.FILLED)
        cv2.circle(img, (cx, cy), 31, yellow, 2)
        cv2.circle(img, (cx, cy), 30, white, cv2.FILLED)

    cv2.imshow("Iron Man", img)

    if cv2.waitKey(1) == ord('q'):
        break