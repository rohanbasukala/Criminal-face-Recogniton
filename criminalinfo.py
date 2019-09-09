from tkinter import *
from tkinter.scrolledtext import ScrolledText
import sqlite3
import os
import sys
#from tkinter.filedialog
from PIL import ImageTk
from PIL import *
from PIL import Image
import datasetCreatorGUI
from tkinter.filedialog import askopenfilename

root = Tk()
root.geometry('500x500')
root.title("Criminal Information")

Id=IntVar()
Name=StringVar()
Age=IntVar()
Gender=StringVar()
Crime=StringVar()

#pyexec=sys.executable

def datasetCreatorGUI():
    Pathpy=filedialog.askopenfilename(title="one a file",filetypes=[('datasetCreatorGUI','.py')])
    #os.system('%s %s' %(pyexec,Pathpy))
    os.system(Pathpy)

#SQLITE
def insertOrUpdate():

    Id1=Id.get()
    Name1=Name.get()
    Age1=Age.get()
    Gender1=Gender.get()
    Crime1=Crime.get()
    
    conn=sqlite3.connect("demo.db")
    cmd="SELECT * FROM criminal WHERE ID=" +str(Id1)
    cursor = conn.execute(cmd)
    idRecordExist=0
    for row in cursor:
        isRecordExist=1
    if(idRecordExist==1):
        cmd="UPDATE People SET Name=" +str(Name1)+"WHERE ID=" +str(Id1)
    else:
        cmd="INSERT INTO criminal(ID,Name,Age,Gender,Crime) VALUES(" +str(Id1) + "," +str(Name1) +"," +str(Age1) +"," +str(Gender1) + "," +str(Crime1) + ")"
    conn.execute(cmd)
    conn.commit()
    conn.close()


label_0 = Label(root, text="CRIMINAL INFORMATION",width=20,font=("bold", 20))
label_0.place(x=90,y=53)


label_1 = Label(root, text="ID",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvar=Id)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Name",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root, textvar=Name)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=70,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=Gender, value=1).place(x=235,y=230)
Radiobutton(root, text="Female",padx = 20, variable=Gender, value=2).place(x=290,y=230)

label_4 = Label(root, text= "Age", width=20,font=("bold", 10))
label_4.place(x=80, y=280)

entry_4 = Entry(root)
entry_4.place(x=240 , y=280)

label_4 = Label(root, text= "Age", width=20,font=("bold", 10))
label_4.place(x=80, y=280)

entry_4 = Entry(root, textvar=Age)
entry_4.place(x=240 , y=280)

label_5 = Label(root, text= "Criminal", width=20,font=("bold", 10))
label_5.place(x=80, y=320)
entry_5 = Entry(root , textvar=Crime)
entry_5.place(x=240 , y=320)

'''
label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)


list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];
c=StringVar()
droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)
'''


Button(root, text='Submit',width=20,bg='black',fg='white', command=insertOrUpdate).place(x=180,y=380)
Button(root, text='Create DataSet',width=20,bg='black',fg='white', command=datasetCreatorGUI).place(x=180,y=420)

root.mainloop()
