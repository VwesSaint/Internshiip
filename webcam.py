from ultralytics import YOLO
import cv2
model = YOLO('yolov8l.pt')
cap = cv2.VideoCapture(0)
while True:
    ret,frame = cap.read()
    results = model(frame,show = True)
    if not ret:
        break
    if cv2.waitKey(1) & 0xFF==ord('q'):``
        break
cap.release()
cv2.destroyAllWindows()