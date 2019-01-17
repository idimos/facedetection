import cv2 as cv
import os

cascadePath = 'Cascades'
facecascadeXML = 'haarcascade_frontalface_default.xml'
eyecascadeXML = 'haarcascade_eye.xml'

facecascade = cv.CascadeClassifier(os.path.join(cascadePath,facecascadeXML))
eyecascade = cv.CascadeClassifier(os.path.join(cascadePath,eyecascadeXML))

cap = cv.VideoCapture(0)
cap.set(3,1024)
cap.set(4,768)

font = cv.FONT_HERSHEY_SIMPLEX

while True:
    ret, img = cap.read()
    img = cv.flip(img,1)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    faces = facecascade.detectMultiScale(gray, 1.2, 6, minSize=(20, 20))

    for(x,y,w,h) in faces:
        cv.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 1)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        eyes = eyecascade.detectMultiScale(roi_gray, 1.5, 10, minSize=(5, 5))

        for(ex, ey, eh, ew) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex+ew,ey+eh), (0,255,0),1)

    cv.putText(img, "LabSTEM Robotics", (10, int(cap.get(4))-15), font, 1, (255, 255, 255), 2)
    cv.imshow('Labstem Windows',img)

    k = cv.waitKey(10)
    if k == 27:
        break

print("\n [Info] Exiting program")
cap.release()
cv.destroyAllWindows()