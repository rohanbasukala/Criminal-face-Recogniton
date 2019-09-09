import numpy as np
import sqlite3
import cv2
import time
from datasetCreatorGUI import *
import sys
from time import sleep
import logging as log
import datetime as dt

video = sys.argv[0]
Cascade = 'C:\\Users\\Rohan\\face recog - Sqlite\\haarcascade_frontalface_default.xml'


face_cascade = cv2.CascadeClassifier(Cascade)
log.basicConfig(filename='dataset_GUI',level=log.INFO)   

#cap = cv2.VideoCapture(0)
video_capture = cv2.VideoCapture(video)
success,image = video_capture.read()
i=0
anterior= 0
path= '/maroon5/'
'''
#SQLITE
def insertOrUpdate(Id, Name,Age, Gender,Crime):
    conn=sqlite3.connect("Face.db")
    cmd="SELECT * FROM People WHERE ID=" +str(Id)
    cursor = conn.execute(cmd)
    idRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(idRecordExist==1):
        cmd="UPDATE People SET Name=" +str(Name)+"WHERE ID=" +str(Id)
    else:
        cmd="INSERT INTO People(ID,Name,Age,Gender,Crime) VALUES(" +str(Id) + "," +str(Name) +"," +str(Age) +"," +str(Gender) + "," +str(Crime) + ")"
    conn.execute(cmd)
    conn.commit()
    conn.close()
    
id = input('Enter User Id')
name = input('Enter User Name')
age= input("enter age:")
gender = input('Enter Gender :')
criminalrec= input('what crime he/she has done ')
               
insertOrUpdate(id,name,age, gender, criminalrec)
'''
sampleNum=0;

while success:
    if not video_capture.isOpened():
        print('Unable to load.')
        sleep(5)
        pass
    
    # ret, img = cap.read()
    success,img = video_capture.read()    
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
        # pass resized_image (nd.array ) to prediction model
        '''
        emotion_count[..]+=1       
        '''
        
       # print(resized_image.size())
    for (x,y,w,h) in faces:
        sampleNum += 1;
        cv2.imwrite("datasets/User." +str(id) + "." + str(sampleNum)+ ".jpg",gray[y:y+h, x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        cv2.waitKey(100)

    cv2.imshow("img",img)
    cv2.waitKey(1)

    if(sampleNum>100):
        break

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
