import numpy as np
import cv2
import urllib.request

url = "http://192.168.1.20:8080/shot.jpg"
cap1 = cv2.VideoCapture(1)
cap2 = cv2.VideoCapture(2)

while True:
    ret, frame1 = cap1.read()
    ret, frame2 = cap2.read()

    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)

    cv2.imshow('ipwebcam', img)
    cv2.imshow('default webcam', frame1)
    cv2.imshow('intex webcam', frame2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap1.release()
cap2.release()
cv2.destroyAllWindows()
