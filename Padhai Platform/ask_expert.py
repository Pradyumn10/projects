from tkinter import*
import tkinter
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk

db=sqlite3.connect('mofos.db')
cur=db.cursor()

top=Tk()
top.geometry("1080x720")

top.overrideredirect(True)
top.resizable(width=False,height=False)

def backbutton():
    top.destroy()
    import homescreen
def data3():
    a1=user.get()
    a2=ques.get("1.0",END)
    cur.execute('''insert into question values(?,?) ''',(a1,a2))
    db.commit()
    messagebox.showinfo("information","Question registered! our expert will reach you out through mail.")
    
c=Canvas(top,bg="#2B2B28",height=1500,width=1500)
c.pack()

zee1=tkinter.StringVar()
zee2=tkinter.StringVar()

label1=Label(top,text="ASK AN EXPERT",font=("Oswald",36),background='#2B2B28',fg="White")
label1.place(x=370,y=50)

label=Label(top,text="YOUR MAIL",font=("Oswald",18),background='#2b2B28',fg="White")
label.place(x=320,y=180)

user=Entry(top,textvariable=zee1,font=("Oswald",10),width=50)
user.place(x=450,y=192)

label=Label(top,text="QUESTION",font=("Oswald",18),background='#2b2B28',fg="White")
label.place(x=320,y=280)

ques=Text(top,font=("Oswald",10),width=50,height=10)
ques.place(x=450,y=290)

label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="White")
label.place(x=10,y=690)

but=Button(top,text="Submit",width=20,command=data3,font=("Oswald",15),background='#82827D',fg="White")
but.place(x=410,y=530)

button_back=Button(top,text="<-",bg="red",command=backbutton)
button_back.place(x=0,y=0)

button_exit=Button(top,text="  X  ",font=("Oswald",10),bg="red",command=top.destroy)
button_exit.place(x=1055,y=0)

a='D:\STUDIES\SEMESTER 3\PYTHON\MOFOS PROJECT\logoo.jpg'
load=Image.open(a)
render=ImageTk.PhotoImage(load)
c.create_image(5,5,anchor=NW,image=render)

top.mainloop()
