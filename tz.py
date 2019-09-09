
import numpy as np
import cv2
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#cap = cv2.VideoCapture(0)
vidcap = cv2.VideoCapture('bb.mp4')

emotion_count={
    "Angry":0,
    "Disgust":0, 
    "Fear":0,
    "Happy":0, 
    "Sad":0, 
    "Surprise":0,
    "Neutral":0
    }

emotion_count=[0,0,0,0,0,0,0]


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
        # pass resized_image (nd.array ) to prediction model
        '''
        emotion_count[..]+=1
        
        
        '''
        
       # print(resized_image.size())
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        
 #
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        
        for k in emotion_count:
           print(k)

        break

vidcap.release()
cv2.destroyAllWindows()
