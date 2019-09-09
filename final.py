import cv2
from PIL import ImageTk
from PIL import *
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import sqlite3
import os
import sys
from os import system
import numpy as np
import PIL.Image
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class faceRecog(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.iconbitmap(self, default = 'iconn.ico' )
        tk.Tk.wm_title(self, "Face recognition")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames={}
        
        for F in (StartPage, PageOne, detect):
            
            frame=F(container, self)

            self.frames[F] = frame

            frame.grid(row=0 , column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

def getvideofile():
    global video
    video = askopenfilename()
    print (video)
    return video
        
def putvideofile():
    global video
    video = askopenfilename()
    print (video)
    return video

class StartPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text = "Face Recognition", font=LARGE_FONT)
        label.pack(padx=10, pady=10)

        button1 = ttk.Button(self, text= "Add Faces" , command=lambda:controller.show_frame(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text= "Detect Faces" , command=lambda:controller.show_frame(detect))
        button2.pack()

#SQLITE
def insertOrUpdate(id1, Name1, Age1, Gender1, Crime1):
    try:
        id1=Id.get()
        Name1=Name.get()
        Age1=Age.get()
        Gender1=Gender.get()
        Crime1=Crime.get()
        
        conn=sqlite3.connect("demo.db")
        cmd="SELECT * FROM criminal WHERE Id=" + str(id1)
        cursor = conn.execute(cmd)
        idRecordExist=0
        for row in cursor:
            isRecordExist=1
        if(idRecordExist==1):
            cmd="UPDATE criminal SET Name=" + str(Name1)+"WHERE Id=" + str(id1)
        else:
            cmd="INSERT INTO criminal(Id,Name,Age,Gender,Crime) VALUES(" +str(id1) + "," +str(Name1) +"," +str(Age1) +"," +str(Gender1) + "," +str(Crime1) + ")"
        conn.execute(cmd)
        conn.commit()
        conn.close()
    except Exception as E:
        print(E)

class PageOne(tk.Frame):
    global Id, Name , Age, Gender , Crime

    def __init__(self,parent,controller):
            tk.Frame.__init__(self, parent)        
            self.parent = parent
            self.initUI()

    def initUI(self):

        Id= IntVar()
        Name = StringVar()
        Age= IntVar()
        Gender= StringVar()
        Crime= IntVar()

        label_0 = ttk.Label(self, text="UPLOAD CRIMINAL INFORMATION",font = LARGE_FONT)
        label_0.grid(column=1, row=1)

        label_1 = ttk.Label(self, text="ID", font = LARGE_FONT)
        label_1.grid(column=1, row=3)
        entry_1 = ttk.Entry(self, textvar=Id)
        entry_1.grid(column=2, row=3)
            
        label_2 = ttk.Label(self, text="Name", font = LARGE_FONT)
        label_2.grid (column=1, row= 4)
        entry_2 = Entry(self, textvar=Name)
        entry_2.grid(column=2, row=4)

        label_3 = Label(self, text="Gender",font = LARGE_FONT)
        label_3.grid(column=1, row=5)
        var = IntVar()
        Radiobutton(self, text="Male",padx = 5, variable=Gender, value=1).grid(column=2, row=5)
        Radiobutton(self, text="Female",padx = 20, variable=Gender, value=2).grid(column=3, row=5)

        label_4 = Label(self, text= "Age",font = LARGE_FONT)
        label_4.grid(column=1, row=6)
        entry_4 = Entry(self, textvar=Age)
        entry_4.grid(column=2, row=6)

        label_5 = Label(self, text= "Crime:",font = LARGE_FONT)
        label_5.grid(column=1, row=7)
        entry_5 = Entry(self , textvar=Crime)
        entry_5.grid(column=2, row=7)

        button_1 = ttk.Button(self, text='Submit', command=lambda: controller.insertOrUpdate(self.Id,self.Name, self.Age, self.Gender, self.Crime))
        button_1.grid(column=2,row=9)
        
def detect(self,video):

        #video = sys.argv[0]
        Cascade = 'C:\\Users\\Rohan\\face recog - Sqlite\\haarcascade_frontalface_default.xml'

        face_cascade = cv2.CascadeClassifier(Cascade)
        #log.basicConfig(filename='detectt',level=log.INFO)   

        #cap = cv2.VideoCapture(0)
        vidcap = cv2.VideoCapture(0)

        rec = cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizer\\trainingData.yml")
        #id=0;
        def getProfile(id):
            conn=sqlite3.connect("demo.db")
            cmd= "SELECT * FROM criminal WHERE Id=" +str(id)
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
                profile = getProfile(id)
                
                #if(conf<50):
                #        profile=getProfile(id)
                #else:
                #       id=0
                #       profile=getProfile(id)
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

class detect(tk.Frame):
    def __init__(self, parent, container):

            tk.Frame.__init__(self, parent)   

            label = tk.Label (self,text='Detect Faces..',font = LARGE_FONT)
            label.pack()

            video_choose_button2 = ttk.Button(self, text='Choose Video',command=lambda:putvideofile())
            video_choose_button2.pack()
            
            #start button_frame
            start_button = ttk.Button(self, text= 'Start', command= lambda:detect())
            start_button.pack()

            back_button = ttk.Button(self, text = 'back', command = lambda : controller.show_frame(StartPage))
            back_button.pack()

app = faceRecog()
app.mainloop()