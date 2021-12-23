import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
detector = HandDetector(detectionCon=0.8)
faceDetector = FaceDetector(minDetectionCon=0.5)
coloR = (0,255,0)
coloR2 = (255,0,0)
color = (0,0,0)
_ = ''
while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img = detector.findHands(img)
    #img = faceDetector.findFaces(img,draw=True)
    lmList, _ = detector.findPosition(img)
    if lmList:
        myHandType = detector.handType()
        #cv2.putText(img,f'Hand:{myHandType}')
        fingerTip = lmList[8]
        if 100<fingerTip[0]<250 and 100<fingerTip[1]<250:
            color = coloR
        else:
            color = coloR2
    cv2.rectangle(img,(100,100),(250,250),color,thickness=cv2.FILLED)
    cv2.imshow("Image",img)


    cv2.waitKey(1)
