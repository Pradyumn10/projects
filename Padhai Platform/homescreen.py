from tkinter import *
import tkinter
from tkinter import messagebox
from PIL import Image,ImageTk

  
top=Tk()
top.geometry("1080x720")

top.overrideredirect(True)
top.resizable(width=False,height=False)

c=Canvas(top,bg="#2B2B28",height=1500,width=1500)
c.pack()


def mathbutton():
    top.destroy()
    import maths

def coabutton():
    top.destroy()
    import coa
   
def discretebutton():
    top.distroy()
    import discrete

def databutton():
    top.destroy()
    import datastructure

def germanbutton():
    top.destroy()
    import german

def pythonbutton():
    top.destroy()
    import pythonprogramming

def dbmsbutton():
    top.destroy()
    import dbms

def backbutton():
    top.destroy()
    import homescreen

def ask_exp():
    top.destroy()
    import ask_expert
    
label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="White")
label.place(x=10,y=690)
label1=Label(top,text="Home Page",font=("Oswald",36),background='#2B2B28',fg="White")
label1.place(x=410,y=40)
#PADAIPLATFORM

button_maths=Button(top,text='Maths',command=mathbutton,width=12,font=("Oswald",15),background='#82827D',fg="White")
button_maths.place(x=230,y=190)


button_pythonprogramming=Button(top,text='Python Programming',command=pythonbutton,width=18,font=("Oswald",15),background='#82827D',fg="White")
button_pythonprogramming.place(x=670,y=190)

button_discrete=Button(top,text='Discrete Structures',command=discretebutton,width=16,font=("Oswald",15),background='#82827D',fg="White")
button_discrete.place(x=120,y=330)

button_data=Button(top,text='Data Structure',command=databutton,width=14,font=("Oswald",15),background='#82827D',fg="White")
button_data.place(x=440,y=330)

button_german=Button(top,text='German',command=germanbutton,width=15,font=("Oswald",15),background='#82827D',fg="White")
button_german.place(x=760,y=330)

button_coa=Button(top,text='COA',command=coabutton,width=12,font=("Oswald",15),background='#82827D',fg="White")
button_coa.place(x=230,y=470)

button_dbms=Button(top,text='DBMS',command=dbmsbutton,width=15,font=("Oswald",15),background='#82827D',fg="White")
button_dbms.place(x=670,y=470)

label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="WHITE")
label.place(x=10,y=690)

button_expert=Button(top,text='Ask an Expert',width=13,font=("Oswald",12),background='#E3B043',fg="White",command=ask_exp)
button_expert.place(x=480,y=670)

button_exit=Button(top,text="  X  ",font=("Oswald",10),bg="red",command=top.destroy)
button_exit.place(x=1055,y=0)

a='D:\STUDIES\SEMESTER 3\PYTHON\MOFOS PROJECT\logoo.jpg'
load=Image.open(a)
render=ImageTk.PhotoImage(load)
c.create_image(5,5,anchor=NW,image=render)

top.mainloop()
