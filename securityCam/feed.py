'''
* @File : feed.py
* @Author : Pradyumn Joshi
* @Brief : Its the script for live feed
* @version : 0.1.0
* @date : 2021-01-15
*
* @copyright (c) 2021
'''

import cv2
import time
from tkinter import *
from PIL import ImageTk,Image
import datetime

#s_time = time.time()

#camera instance
source = 0
cap = cv2.VideoCapture(source)

def videoStream():
    '''
    It shows frame in Label
    '''

    ret,frame = cap.read()
    rgbaFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGBA)
    
    font = cv2.FONT_HERSHEY_SIMPLEX
    
    #cv2.putText(frame, f'{datetime.datetime.now().strftime("%D-%H-%M-%S")}', (225, 110), font, 1, (255, 255, 255), 2,cv2.LINE_4)
    
    #cv2.imshow("frame", frame)
    #mirroring the frame
    flipFrame = cv2.flip(rgbaFrame,1)
    
    #Setting the image in Label
    img = Image.fromarray(flipFrame)
    imgTk = ImageTk.PhotoImage(image=img)
    labelVideo.imgtk = imgTk
    labelVideo.configure(image=imgTk)

    #width  = cap.get(3)
    #height = cap.get(4)
    #print(width, height)

    labelVideo.after(1,videoStream)

def backbutton():
    top.destroy()
    cap.release()
    import home.py

#creating tkinter instance
top = Tk()
top.geometry("1080x720")
top.resizable(width=False, height=False)

#creating canvas
canvas= Canvas(top,bg="#2B2B28", height=1500, width=1500)
canvas.pack()

#label
labelName = Label(top, text= "Live Camera Feed", width=18, background="#2B2B28", fg="White")
labelName.place(x=500,y=40)

#label for datetime
labelDate = Label(top, text=f'{datetime.datetime.now().strftime("%D-%H-%M-%S")}', width=200, background="#2B2B28", fg="White")
labelDate.place(x=20,y=82)

#label for video
labelVideo = Label(top, width=640,height=480, background="#2B2B28")
labelVideo.place(x=215, y=110)
videoStream()

#back button
labelBack=Button(top,text="<-",bg="red",command=backbutton)
labelBack.place(x=0,y=0)

#exit button
buttonExit = Button(top, text="X", bg="red", command=top.destroy)
buttonExit.place(x=1052,y=0)

top.mainloop()

cap.release()
cv2.destroyAllWindows()
