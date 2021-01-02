import tkinter
from tkinter import *
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk

db=sqlite3.connect('mofos.db')
cur=db.cursor()

def backbutton():
    top.destroy()
    import login 

def data():
    global cur
    global db
    a1=name.get()
    a2=contact.get()
    a3=university.get()
    a4=user.get()
    a5=pas.get()
    if(not a1=="" and not a4=="" and not a5==""):
        cur.execute('''insert into registration_table(u_name,u_con,u_univ,u_user,u_pass) values(?,?,?,?,?)''',(a1,a2,a3,a4,a5))
        db.commit()
        print("Data saved")
        messagebox.showinfo("information","Welcome to PADAI PLATFORM")
        import homescreen
        
    else:
        print("")
        messagebox.showinfo("Error","Enter values First")


print("Connected to MYSQL!")
top=tkinter.Tk()
top.geometry("1080x720")
top.overrideredirect(True)
top.resizable(width=False,height=False)

c=Canvas(top,background="#2B2B28",height=1500,width=1500)
c.pack()

zee1=tkinter.StringVar()
zee2=tkinter.StringVar()
zee3=tkinter.StringVar()
zee4=tkinter.StringVar()
zee5=tkinter.StringVar()

label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="White")
label.place(x=10,y=690)
label1=Label(top,text="Registeration Form",font=("Oswald",36),background='#2B2B28',fg="White")
label1.place(x=350,y=50)

#name
label_name=Label(top,text="Name",font=("Oswald",18),background='#2b2B28',fg="White")
label_name.place(x=300,y=150)
name=Entry(top,width=40,textvariable=zee1,font=("Oswald",10))
name.place(x=430,y=165)

#contact
label_contact=Label(top,text="Contact No.",font=("Oswald",18),background='#2b2B28',fg="White")
label_contact.place(x=300,y=210)
contact=Entry(top,width=40,textvariable=zee2,font=("Oswald",10))
contact.place(x=430,y=225)

#university
label_university=Label(top,text="University",font=("Oswald",18),background='#2b2B28',fg="White")
label_university.place(x=300,y=270)
university=Entry(top,width=40,textvariable=zee3,font=("Oswald",10))
university.place(x=430,y=285)

#username
label_user=Label(top,text="E-mail",font=("Oswald",18),background='#2b2B28',fg="White")
label_user.place(x=300,y=330)
user=Entry(top,width=40,textvariable=zee4,font=("Oswald",10))
user.place(x=430,y=345)

#password
label_pass=Label(top,text="Password",font=("Oswald",18),background='#2b2B28',fg="White")
label_pass.place(x=300,y=390)
pas=Entry(top,width=40,textvariable=zee5,font=("Oswald",10),show='*')
pas.place(x=430,y=405)

#button
but=Button(top,text="Submit",width=20,command=data,font=("Oswald",15),background='#82827D',fg="White")
but.place(x=420,y=480)

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

        
