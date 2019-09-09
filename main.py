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
from tkinter import ttk,BOTH

global idz
idz=0

video = sys.argv[0]
Cascade = 'C:\\Users\\Rohan\\face recog - Sqlite\\haarcascade_frontalface_default.xml'



def getvideofile():
	global video
	video = askopenfilename()
	print (video)
	return video

'''
def getcascadefile():
	global Cascade
	Cascade = askopenfilename()
	print (Cascade)
	return Cascade
'''


def putvideofile():
	global video
	video = askopenfilename()
	print (video)
	return video

def datasetCreator():
        system('python dataset_GUI.py')

     
#SQLITE
def insertOrUpdate(id1, Name1, Age1, Gender1, Crime1):

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
                cmd="UPDATE criminal SET Name=" +str(Name1)+"WHERE Id=" +str(id1)
            else:
                cmd="INSERT INTO criminal(Id,Name,Age,Gender,Crime) VALUES(" +str(id1) + "," +str(Name1) +"," +str(Age1) +"," +str(Gender1) + "," +str(Crime1) + ")"
            conn.execute(cmd)
            conn.commit()
            conn.close()

def aa (video, Cascade):


        face_cascade = cv2.CascadeClassifier(Cascade)
        video_capture = cv2.VideoCapture(video)
        Id=IntVar()
        success,image = video_capture.read()
        i=0
        anterior= 0
        #path= '/maroon5/'
        
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
           # if (Id== 0):
            #        Id+=1
                    
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
                          
               # print(resized_image.size())
               
            for (x,y,w,h) in faces:
                sampleNum += 1;
                cv2.imwrite("datasets/User." + str(entry_1.get()) + "." + str(sampleNum)+ ".jpg" ,gray[y:y+h, x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.waitKey(5)
                #print('first' + idz)


            cv2.imshow("img",img)
            #if(cv2.waitKey(1)==ord('q')):
             #       break;

            if(sampleNum>70):
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
           
 
        video_capture.release()
        cv2.destroyAllWindows()

def camera(Cascade):

        face_cascade = cv2.CascadeClassifier(Cascade)
        video_capture = cv2.VideoCapture(0)
        Id=IntVar()
        success,image = video_capture.read()
        i=0
        anterior= 0
        #path= '/maroon5/'
        
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
           # if (Id== 0):
            #        Id+=1
                    
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
                          
               # print(resized_image.size())
               
            for (x,y,w,h) in faces:
                sampleNum += 1;
                cv2.imwrite("datasets/User." + str(entry_1.get()) + "." + str(sampleNum)+ ".jpg" ,gray[y:y+h, x:x+w])
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                cv2.waitKey(5)
                #print('first' + idz)


            cv2.imshow("img",img)
            #if(cv2.waitKey(1)==ord('q')):
             #       break;

            if(sampleNum>70):
                break

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
           

        video_capture.release()
        cv2.destroyAllWindows()

        
def detect(video):
        face_cascade = cv2.CascadeClassifier(Cascade)
        #log.basicConfig(filename='detectt',level=log.INFO)   

        #cap = cv2.VideoCapture(0)
        vidcap = cv2.VideoCapture(video)

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
                
                #profile = getProfile(id)

                if(conf<50):
                        profile=getProfile(id)
                else:
                        id=0
                        profile=getProfile(id)

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


def trainer():
        recognizer = cv2.face.LBPHFaceRecognizer_create();
        #recognizer = cv2.create_LBPHFaceRecognizer();

        path= 'datasets'

        def getImageWithID(path):
            imagePaths= [os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            IDs=[]

            for imagePath in imagePaths:
                    
                faceImg=PIL.Image.open(imagePath).convert('L');
                faceNp= np.array(faceImg,'uint8')
                Id=int(os.path.split(imagePath)[-1].split('.')[1])
                faces.append(faceNp)
                IDs.append(Id)
                cv2.imshow("training", faceNp)
                cv2.waitKey
            return IDs, faces

        Ids,faces = getImageWithID(path)
        recognizer.train(faces, np.array(Ids))
        recognizer.save('recognizer/trainingData.yml')
        cv2.destroyAllWindows()

def camera_detect():
        face_cascade = cv2.CascadeClassifier(Cascade)
        #log.basicConfig(filename='detectt',level=log.INFO)   

        #cap = cv2.VideoCapture(0)
        vidcap = cv2.VideoCapture(0)

        rec = cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizer\\trainingData.yml")
        
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
                
                #profile = getProfile(id)

                if(conf<50):
                        profile=getProfile(id)
                else:
                        id=0
                        profile=getProfile(id)

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


if __name__ == '__main__':
    try:
            
        root = tk.Tk()
        #root.overrideredirect(True)
        #root.geometry("{1}x{1}+0+0".format(root.winfo_screenwidth(),root.winfo_screenheight()))
        root.geometry("1500x800+0+0")
        root.title("Criminal Identification")

        Id = IntVar()
        Name = StringVar()
        Age = IntVar()
        Gender = StringVar()
        Crime = StringVar()
        
        idz=0

        ####################FRAMEEE#################################
        tops = Frame(root, width = 1000, height = 100, bd=10, relief= "raise")
        tops.pack(side=  TOP,fill = BOTH)

        lefts = Frame(root , width =700, height = 700, bd= 5, relief= "raise" )
        lefts.pack(side= LEFT, fill = BOTH, expand = True)

        rights = Frame ( root , width = 300 , height = 700, bd= 5, relief="raise")
        rights.pack(side= RIGHT, fill = BOTH)


        #insertOrUpdate(Id, Name, Age, Gender, Crime)
        
        leftFrame = Frame(lefts, width = 700, height = 300, bd=5, relief="raise")
        leftFrame.pack(side= TOP, fill = BOTH)

        middleFrame=Frame(lefts, width=700, height=200, bd=5, relief="raise")
        middleFrame.pack(side = TOP, fill = BOTH)
    

        rightFrame = Frame(rights, width=300, height=700, bd=8 , relief="raise")
        rightFrame.pack(side= TOP, fill = BOTH)
        
        downFrame = Frame(rights, width=700, height=700, bd=8 , relief="raise")
        downFrame.pack (side= TOP, fill = BOTH)
        
        cameraFrame = Frame(lefts, width=800, height=700, bd=8 , relief="raise")
        cameraFrame.pack(side= TOP, fill = BOTH)
        
        detectcameraFrame = Frame(lefts, width=800, height=300, bd=8 , relief="raise")
        detectcameraFrame.pack(side=TOP, fill = BOTH)
        '''      
        image_label = tk.Label(master=leftFrame)
        image_label.grid(column=1, row=1)
        background = ImageTk.PhotoImage(file='criminal.jfif')
        image_label['image'] = background
        '''
        #Data Entry
        label_0 = Label(tops, text="CRIMINAL IDENTIFICATION USING FACIAL RECOGNITION..",font=('arial' , 40,"bold"))
        label_0.grid(row=0,column = 0)
        
        label_0 = Label(rightFrame, text="CRIMINAL INFORMATION",width=20,font=("bold", 20))
        label_0.grid(column=1, row=1)

        label_1 = Label(rightFrame, text="ID",width=20,font=("bold", 10))
        label_1.grid(column=1, row=3)


        def return_entry():
                global idz
                entry_1 = idz.get()
                print(idz)
        
        entry_1 = Entry(rightFrame, textvar=Id)
        entry_1.grid(column=2, row=3)
        #idz = entry_1.get()
        #print(idz)
        
        entry_1.bind('<Return>',return_entry)

        
        label_2 = Label(rightFrame, text="Name",width=20,font=("bold", 10))
        label_2.grid(column=1, row=4)

        entry_2 = Entry(rightFrame, textvar=Name)
        entry_2.grid(column=2, row=4)

        label_3 = Label(rightFrame, text="Gender",width=20,font=("bold", 10))
        label_3.grid(column=1, row=5)
        var = IntVar()
        Radiobutton(rightFrame, text="Male",padx = 5, variable=Gender, value=1).grid(column=2, row=5)
        Radiobutton(rightFrame, text="Female",padx = 20, variable=Gender, value=2).grid(column=3, row=5)

        label_4 = Label(rightFrame, text= "Age:", width=20,font=("bold", 10))
        label_4.grid(column=1, row=6)

        entry_4 = Entry(rightFrame, textvar=Age)
        entry_4.grid(column=2, row=6)

        label_5 = Label(rightFrame, text= "Crime:", width=20,font=("bold", 10))
        label_5.grid(column=1, row=7)
        entry_5 = Entry(rightFrame , textvar=Crime)
        entry_5.grid(column    =2, row=7)
        
        #image_label = PhotoImage(master = leftFrame, file= "criminal.jfif")
        #root.create_image(20, 20, anchor = NW, image = image_label)

        
        image_label = tk.Label(master=leftFrame)
        image_label.grid(row= 1, column = 2)
        background = ImageTk.PhotoImage(file='criminal.jfif')
        image_label['image'] = background
               
        button_frame1 = tk.Frame(leftFrame)
        button_frame1.grid(row=2, column= 2)
       
        video_choose_button1 = tk.Button(master=button_frame1, width= 22, text='Choose Video',command=lambda: getvideofile())
        video_choose_button1.grid(row= 1, column = 2)
       
        start_button = tk.Button(master=button_frame1, width= 30,text='Start', command=lambda: aa(video , Cascade))
        start_button.grid(column=2, row=2)
        #root.mainloop()

        
        button_frame2 = tk.Frame(middleFrame)
        button_frame2.grid(column=1, row=1) 
       
        video_choose_button2 = ttk.Button(master=button_frame2, width= 22,text='Choose Video',command=lambda: putvideofile())
        video_choose_button2.grid(column=1, row=3)
        

        #start button_frame
        start_button = ttk.Button(master=button_frame2, width= 22,text= 'Start', command= lambda : detect(video))
        start_button.grid(column=1, row=4)
        
        

        dataInput = ttk.Button(rightFrame, text='Submit',width=22, command=lambda: insertOrUpdate(Id, Name, Age, Gender, Crime))
        dataInput.grid(column=2,row=9)
        #Button(root, text='Create DataSet',width=20,bg='black',fg='white', command=datasetCreatorGUI).place(x=180,y=420)
        #print('secomd'+idz)

        trainlabel = tk.Label(downFrame, text= "Training ", font=("bold", 10)).grid(column=1, row=1)
        trainButton = ttk.Button(downFrame, text= "Train", width = 22 , command= trainer).grid(column=1, row=4)


        button_frame_camera = tk.Frame(cameraFrame)
        button_frame_camera.grid(column=1, row=2)
        
        image_label1 = tk.Label(master=cameraFrame)
        image_label1.grid(row= 1, column = 2)
        background = ImageTk.PhotoImage(file='face2image.jpg')
        image_label1['image'] = background

        cameralabel01 = Label(cameraFrame, text= "Using Camera", font =("arial", 20, "bold"))
        cameralabel01.grid(row=1 , column=1)

        start_button_camera = ttk.Button(master=button_frame_camera,text='Start', width= 22, command=lambda: camera(Cascade))
        start_button_camera.grid(column=2, row=5)

        button_frame_detect_camera = tk.Frame(detectcameraFrame)
        button_frame_detect_camera.grid(column=1, row=2)
        
        start_button_detect_camera = ttk.Button(master=button_frame_detect_camera,width= 22, text= 'Start detectcing face', command= lambda: camera_detect())
        start_button_detect_camera.grid(row= 1, column=1)
        root.mainloop()
        
    except Exception as e:
        print (e)
'''
    
    sys.argv = [video, Cascade]
    #execfile('webcam_cv3.py')
    exec(open('dataset_GUI.py').read())

    sys.argv = [video]
    #execfile('webcam_cv3.py')
    exec(open('detectt.py').read())
'''
    # from webcam_cv3 import *
