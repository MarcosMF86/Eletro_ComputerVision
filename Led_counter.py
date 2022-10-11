import numpy
import serial
import cvzone
import cv2
from cvzone.HandTrackingModule import HandDetector
import matplotlib.pyplot as plt

#inicia a captura via webcam
cap = cv2.VideoCapture(0) 
#inicia a comunicação com Arduino
#serialcomm = serial.Serial('COM11', 9600) 
#serialcomm.timeout = 1
#configuração do detector
detector = HandDetector(detectionCon=0.8,maxHands=1)
#inicializa contador
w = 0

while True:
    success, img = cap.read() #leitura da imagem
    img=cv2.resize(img,(800, 600)) #dimensiona janela
    hands, img = detector.findHands(img,draw=True) 
    if hands: 
        hand1 = hands[0]
        #armazena em um vetor quais dedos estão levantados 
        f = detector.fingersUp(hand1)         
        w=0
        e='\n'#delimitador de dado transmitido
        for q in f:
            w+=q 
        #serialcomm.write(e.encode())
        #serialcomm.write(str(w).encode())
    cv2.putText(img, "Total: " + str(int(w)), (10,70), 
    cv2.FONT_HERSHEY_PLAIN, 3, (0,0,255), 3)    
    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):#apertar "q" para encerrar 
        break
