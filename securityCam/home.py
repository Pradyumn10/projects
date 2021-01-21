#home file
#import cv2
from tkinter import *
import time
from PIL import ImageTk, Image
s_time = time.time()

def CameraFunc():
    top.destroy()
    import feed.py

def detectionFunc():
    top.destroy()
    import detection.py

#creating tkinter instance
top = Tk()
top.geometry("1080x720")
#top.overrideredirect(True)
top.resizable(width=False, height=False)

#creating canvas
c = Canvas(top, bg="#2B2B28", height=1500, width=1500)
c.pack()

#creating GUI
label = Label(top, text="Security Camera", background="#2B2B28", fg="White")
label.place(x=500,y=40)

buttonCamera = Button(top, text="Camera Feed", command=CameraFunc, width=12, background="#82827D", fg="White")
buttonCamera.place(x=250,y=190)

buttonDetection = Button(top, text="Face Detection", command=detectionFunc, width=12, background="#82827D", fg="White")
buttonDetection.place(x=700,y=190)



#exit button
buttonExit = Button(top, text="X", bg="red", command = top.destroy)
buttonExit.place(x=1052,y=0)

top.mainloop()


