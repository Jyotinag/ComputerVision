from cvzone.FaceDetectionModule import FaceDetector
import cv2
detector = FaceDetector(minDetectionCon=0.5)
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

while True:
    success, img = cap.read()
    img = cv2.flip(img,1)
    img, bbox = detector.findFaces(img,draw=True)
    #print(bbox)
    cv2.imshow("Image2",img)
    cv2.waitKey(1)
