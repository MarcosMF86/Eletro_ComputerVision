import numpy as np
import serial
import cvzone
import math
import cv2
from cvzone.HandTrackingModule import HandDetector
import matplotlib.pyplot as plt
cap = cv2.VideoCapture(0)
#serialcomm = serial.Serial('COM17', 9600)
#serialcomm.timeout = 1
bar = 400
length = 0
detector = HandDetector(detectionCon=0.8,maxHands=2)# num de mãos
while True:
    success, img = cap.read()
    img=cv2.resize(img,(1000, 800))
    hands, img = detector.findHands(img,draw=True)
    if len(hands)==2:#se detectar alguma mão
        hand1 = hands[0]
        hand2 = hands[1]
        lmlist1 = hand1["lmList"]
        lmlist2 = hand2["lmList"]
        length, info, img = detector.findDistance(lmlist1[8], lmlist2[8],img)
        e='\n'
        bar = np.interp(length, [50, 255], [400, 150])
        bar_per = np.interp(length, [50, 255], [0, 100])#percentual
        bar_per = int(bar_per)
        #serialcomm.write(e.encode())
        #serialcomm.write(str(bar_per).encode())
        cv2.rectangle (img, (50,150), (85,400), (255,0,0), 3)
        cv2.rectangle (img, (50,int(bar)), (85,400), (255,0,0), cv2.FILLED)
        cv2.putText(img, f'PWM {int(bar_per)}%', (20,450), 
        cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)
    cv2.imshow("Image", img)
    #cv2.waitKey(10)
    if cv2.waitKey(1) == ord('a'):
        break
