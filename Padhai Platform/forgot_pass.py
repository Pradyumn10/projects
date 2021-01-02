import tkinter
from tkinter import*
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk

db=sqlite3.connect('mofos.db')
cur=db.cursor()

def backbutton():
    top.destroy()
    import login
    
def data2():
    global cur
    global db
    a1=user.get()
    a2=pas.get()
    a3=re_pas.get()
    try:
        query=" update registration_table set u_pass='"+a2+"' where u_user='"+a1+"' "
        cur.execute(query)
        db.commit()
    except:
        messagebox.showinfo("error","Username Invalid")
    else:
        messagebox.showinfo("information","Password changed")
    
top=Tk()
top.geometry("1080x720")
top.overrideredirect(True)
top.resizable(width=False,height=False)

c=Canvas(top,bg="#2b2B28",height=1500,width=1500)
c.pack()

zee1=tkinter.StringVar()
zee2=tkinter.StringVar()
zee3=tkinter.StringVar()

label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="White")
label.place(x=10,y=690)
label1=Label(top,text="Forgot Password",font=("Oswald",36),background='#2B2B28',fg="White")
label1.place(x=420,y=50)

#username
label_user=Label(top,text="E-mail",font=("Oswald",18),background='#2b2B28',fg="White")
label_user.place(x=320,y=150)
user=Entry(top,width=40,font=("Oswald",10),textvariable=zee1)
user.place(x=440,y=165)

#password
label_pass=Label(top,text="Password",font=("Oswald",18),background='#2b2B28',fg="White")
label_pass.place(x=320,y=210)
pas=Entry(top,width=40,font=("Oswald",10),textvariable=zee2,show='*')
pas.place(x=440,y=225)

#re-password
label_pass1=Label(top,text="Re-enter",font=("Oswald",18),background='#2b2B28',fg="White")
label_pass1.place(x=320,y=270)
re_pas=Entry(top,width=40,font=("Oswald",10),textvariable=zee3,show='*')
re_pas.place(x=440,y=285)

#button
but1=Button(top,text="Submit",width=20,font=("Oswald",15),background='#82827D',fg="White",command=data2)
but1.place(x=450,y=350)

#button for back
button_back=Button(top,text="<-",bg="red",command=backbutton)
button_back.place(x=0,y=0)

#button for exit
button_exit=Button(top,text="X",bg="red",command=top.destroy)
button_exit.place(x=1060,y=0)

a='D:\STUDIES\SEMESTER 3\PYTHON\MOFOS PROJECT\logoo.jpg'
load=Image.open(a)
render=ImageTk.PhotoImage(load)
c.create_image(5,5,anchor=NW,image=render)

top.mainloop()
