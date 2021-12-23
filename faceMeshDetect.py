from cvzone.FaceMeshModule import FaceMeshDetector
import cv2

cap = cv2.VideoCapture(0)
detector = FaceMeshDetector()

while True:
    success, img = cap.read()
    img, _ = detector.findFaceMesh(img)
    cv2.imshow("Image3",img)
    cv2.waitKey(1)