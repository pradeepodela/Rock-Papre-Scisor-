import cv2
import time
import cvzone
from cvzone.HandTrackingModule import HandDetector
# import Randam

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

detecator = HandDetector(maxHands=1)

timer = 0
StartGame = False
StateResult = False
score = [0,0]

while True:
    imagebackground = cv2.imread('Resources/VS.png')
    imagebackground = cv2.resize(imagebackground, (1500, 750))
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    frame = cv2.resize(frame, (0, 0), None, 0.875, 0.875)
    frame = frame[:, 80:480]

    # frame = cv2.resize(frame, (496, 496))

    imagebackground[434:854, 795:1195] = frame

    cv2.imshow('frame', frame)
    cv2.imshow('background', imagebackground)
    key = cv2.waitKey(1)
    if  key == ord('s'):
        cv2.distroyAllWindows()
        cap.release()
        break

    

