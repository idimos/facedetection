import numpy as np
import cv2
from gpiozero import Servo
from time import sleep
servo = Servo(14)

face_cascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

cap.set(3,640) # set Width
cap.set(4,480) # set Height

LEFT = int((cap.get(3)/2) - (cap.get(3)/6))
RIGHT = int((cap.get(3)/2) + (cap.get(3)/6))

def cb(d):
    if d == 1:
        print("ERROR LEFT")
        servo.min()
        sleep(1)
        servo.mid()
    elif d == 2:
        print("ERROR RIGHT")
        servo.max()
        sleep(1)
        servo.mid()        

def watch(cx,cb=None):
    if cx<= LEFT:
        cb(1)
    elif cx >= RIGHT:
        cb(2)
        
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    cv2.rectangle(img,(int(cap.get(3)/3),int(cap.get(4)/3)),(int((cap.get(3)*2)/3),int((cap.get(4)*2)/3)),(0,255,0),2)


    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cx = int(x+w/2)
        cy = int(y+h/2)
        cv2.circle(img,(cx,cy),5,(0,0,255),-1)
        print(cx,cy)
        
        watch(cx,cb)

    sleep(1)
    cv2.imshow('img',img)
    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()