from tkinter import *
import webbrowser
from PIL import Image,ImageTk

top=Tk()
top.geometry("1080x720")

top.overrideredirect(True)
top.resizable(width=False,height=False)

url1 = 'https://www.youtube.com/playlist?list=PLhSp9OSVmeyLke5_cby8i8ZhK8FHpw3qs'
url2='https://www.youtube.com/watch?v=v2rxQMV14-o'
url3='https://www.youtube.com/playlist?list=PLhSp9OSVmeyJoNnAqghUK-Lit3qBgfa6o'
url4='https://www.youtube.com/playlist?list=PLhSp9OSVmeyJoNnAqghUK-Lit3qBgfa6o'
url5='https://www.youtube.com/playlist?list=PLhSp9OSVmeyJ5N-JUEZj7uS6IAT9a79nD'

def backbutton():
    top.destroy()
    import homescreen 

def click1():
    webbrowser.open_new(url1)

def click2():
    webbrowser.open_new(url2)

def click3():
    webbrowser.open_new(url3)

def click4():
    webbrowser.open_new(url4)

def click5():
    webbrowser.open_new(url5)

c1=Canvas(top,background='#E3B043',height=1500,width=300)
c1.pack(side="left",fill="both")
c2=Canvas(top,background='#2B2B28',height=1500,width=950)
c2.pack(side="right",fill="both")

centerlabel=Label(top,text="MATHS",font=("Oswald",45),background='#2B2B28',fg="White")
centerlabel.place(x=450,y=20)
topic11=Label(top,text="UNIT 1 :- ",font=("Oswald",20),background='#E3B043',fg='#2B2B28')
topic11.place(x=140,y=155)
topic12=Button(top,text="FOURIRER SERIES",font=("Oswald",18),background='#2B2B28',fg="White",command=click1)
topic12.place(x=350,y=140)

topic21=Label(top,text="UNIT 2 :- ",font=("Oswald",20),background='#E3B043',fg='#2B2B28')
topic21.place(x=140,y=245)
topic22=Button(top,text="PARTIAL DIFFERENTIAL EQUATION",font=("Oswald",18),background='#2B2B28',fg="White",command=click2)
topic22.place(x=350,y=240)

topic31=Label(top,text="UNIT 3 :- ",font=("Oswald",20),background='#E3B043',fg='#2B2B28')
topic31.place(x=140,y=345)
topic32=Button(top,text="ONE DIMENSIONAL WAVE AND HEAT EQUATIONS",font=("Oswald",18),background='#2B2B28',fg="White",command=click3)
topic32.place(x=350,y=340)

topic4=Label(top,text="UNIT 4 :- ",font=("Oswald",20),background='#E3B043',fg='#2B2B28')
topic4.place(x=140,y=445)
topic32=Button(top,text="TWO DIMENSIONAL WAVE EQUATION",font=("Oswald",18),background='#2B2B28',fg="White",command=click4)
topic32.place(x=350,y=440)

topic5=Label(top,text="UNIT 5 :- ",font=("Oswald",20),background='#E3B043',fg='#2B2B28')
topic5.place(x=140,y=545)
topic32=Button(top,text="FOURIER TRANSFORM",font=("Oswald",18),background='#2B2B28',fg="White",command=click5)
topic32.place(x=350,y=540)

label=Label(top,text="©GAMING GEEKS",background='#E3B043',fg="#2B2B28")
label.place(x=10,y=690)

button_back=Button(top,text="<-",bg="red",command=backbutton)
button_back.place(x=0,y=0)

button_exit=Button(top,text="X",bg="red",command=top.destroy)
button_exit.place(x=1060,y=0)

a='D:\STUDIES\SEMESTER 3\PYTHON\MOFOS PROJECT\logoo.jpg'
load=Image.open(a)
render=ImageTk.PhotoImage(load)
c1.create_image(5,5,anchor=NW,image=render)

top.mainloop()
