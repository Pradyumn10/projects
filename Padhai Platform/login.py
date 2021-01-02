from tkinter import*
import tkinter
from tkinter import messagebox
import sqlite3
from PIL import Image,ImageTk

db=sqlite3.connect('mofos.db')
cur=db.cursor()



def register_window():
    top.destroy()
    import registration
    

def forgot_window():
    top.destroy()
    import forgot_pass
    
def data1():
    global cur
    global db
    a1=user.get()
    a2=pas.get()
    query="select * from registration_table where u_user='"+a1+"' and u_pass='"+a2+"' "
    a=cur.execute(query)
    if cur.fetchone() is not None:
        messagebox.showinfo("information","Welcome to PADAI PLATFORM")
        top.destroy()
        import homescreen
    else:
        messagebox.showinfo("error","Login unSuccessful")

            
        
top=Tk()
top.geometry("1080x720")
top.overrideredirect(True)
top.resizable(width=False,height=False)
c=Canvas(top,background='#2B2B28',height=1500,width=1500)
c.pack()


zee1=tkinter.StringVar()
zee2=tkinter.StringVar()
zee3=tkinter.StringVar()

label=Label(top,text="©GAMING GEEKS",background='#2B2B28',fg="White")
label.place(x=10,y=690)
label1=Label(top,text="LOGIN",font=("Oswald",36),background='#2B2B28',fg="white")
label1.place(x=400,y=60)

#username
label_user=Label(top,text="E-mail",font=("Oswald",18),background='#2b2B28',fg="White")
label_user.place(x=320,y=200)
user=Entry(top,width=40,textvariable=zee1,font=("Oswald",10))
user.place(x=420,y=215)

#password
label_pass=Label(top,text="Password",font=("Oswald",18),background='#2b2B28',fg="White")
label_pass.place(x=320,y=280)
pas=Entry(top,width=40,textvariable=zee2,font=("Oswald",10),show="*")
pas.place(x=420,y=295)

#button
but1=Button(top,text="Submit",width=18,command=data1,font=("Oswald",15),background='#82827D',fg="White")
but1.place(x=430,y=360)

#button
but2=Button(top,text="Forgot Password",width=18,command=forgot_window,font=("Oswald",12),background='#82827D',fg="White")
but2.place(x=340,y=440)

#button
but3=Button(top,text="Not a registered user? Register",width=30,command=register_window,font=("Oswald",12),background='#82827D',fg="White")
but3.place(x=520,y=440)

#label for exit
button_exit=Button(top,text="X",bg="red",command=top.destroy)
button_exit.place(x=1060,y=0)

a='D:\STUDIES\SEMESTER 3\PYTHON\MOFOS PROJECT\logoo.jpg'
load=Image.open(a)
render=ImageTk.PhotoImage(load)
c.create_image(5,5,anchor=NW,image=render)

top.mainloop()

    
