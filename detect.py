import numpy as np
import cv2
from PIL import Image

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default')
cap=cv2.VideoCapture('maroon5.mkv')
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainingData.yml")
id=0
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
fontscale=1
fontcolor = (255 , 255, 255)
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.5, 5)
    #faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        if(id==2):
            id="Gayatri"
        if id==1:
            id="alok"
        if id==3:
            id="anjali"
        if id==4:
            id="Gaurav"
        if id==5:
            id='rahul'
        if id==6:
            id="akshay"
            
        cv2.PutText(img,str(id),(x,y+h),font,fontscale, fontcolor)
    cv2.imshow('img',img)
    
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()

cv2.destroyAllWindows()
