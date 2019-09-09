import sqlite3
import numpy as np
import cv2
import time

video=sys.argv[0]

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#log.basicConfig(filename='detectt',level=log.INFO)   

#cap = cv2.VideoCapture(0)
vidcap = cv2.VideoCapture(video)

rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainingData.yml")
id=0;

def getProfile(id):
    conn=sqlite3.connect("demo.db")
    cmd= "SELECT * FROM criminal WHERE ID=" +str(id)
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
         profile=row
    conn.close()
    return profile

#font= cv2.InitFont(cv2.CV_FONT_HERSEY_COMPLEX_SMALL,1,1,0,1)
font = cv2.FONT_HERSHEY_SIMPLEX
fontscale=1.5
fontcolor = (0,0,255)
success,image = vidcap.read()
while success:
        
    # ret, img = cap.read()
    success,img = vidcap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print(len(gray[479])*640)
    #print(type(faces))
    
    if(len(faces)>0):
        print(faces[0])
        y=faces[0][1]
        x=faces[0][0]
        w=faces[0][2]
        h=faces[0][3]
        crop_img = img[y:y+h, x:x+w]
        cv2.imshow("cropped.jpg", crop_img)
        resized_image = cv2.resize(crop_img, (48, 48)) 
        cv2.imshow("resized_image",resized_image)
        print(len(resized_image))
        print(len(resized_image[0]))

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h, x:x+w])
    
      #  if(conf<50):
        profile=getProfile(id)
       # else:
        #    id=0
         #   profile=getProfile(id)

        if(profile!=None):
            cv2.putText(img,str(profile[1]),(x,y+h+30),font,fontscale, fontcolor)
            cv2.putText(img,str(profile[2]),(x,y+h+60),font,fontscale, fontcolor)
            cv2.putText(img,str(profile[3]),(x,y+h+90),font,fontscale, fontcolor)
            cv2.putText(img,str(profile[4]),(x,y+h+120),font,fontscale, fontcolor)
     
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):

        break
    
vidcap.release()
cv2.destroyAllWindows()
