"""
*  @file faceDetection.py
*  @author Pradyumn Joshi
*  @brief Basic facial recognition system using OpenCV
*  @version 0.1.0
*  @date 2020-08-8
*
*  @copyright Copyright (c) 2020
"""
import cv2
import numpy
import time
from tkinter import *
from threading import Thread
from PIL import ImageTk, Image

class ThreadedCamera(object):
    """
    Face detection and its result
    """
    def __init__(self):
        """
        Initialized source, thread
        """
        self.source = 0
        self.openCam = cv2.VideoCapture(self.source)
        self.ret = False
        self.frame = None
        self.thread = Thread(target = self.camera, daemon = True)
        self.thread.start()

    def camera(self):
        """
        Opens camera and starts reading frames
        """
        while True:
            if self.openCam.isOpened():
                (self.ret, self.frame) = self.openCam.read()

    def frames(self):
        """
        sends frame to Detection 
        Returns:
            frame: grabbed frame
        """
        if self.ret:
            return self.frame


class Detection():
    """
    It detects the face from captured images
    """
    def __init__(self):
        """
        Initialized threaded camera class, image count, haarcascade
        """
        self.cam = ThreadedCamera()
        self.count = 0
        self.cascadeFile = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") 
        #self.frame = self.cam.frames()

    def detectFrame(self):
        """
        It grabs the frame and processes it 
        """
  
        while(True):
            
            frame = self.cam.frames()

            if frame is not None:

                #cv2.imshow("frame" ,frame)
                                            
                gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                t, frames = self.findFace(gray_frame,frame)
                #return gray_frame,frame
                
                #if cv2.waitKey(1) &0xFF == ord("q"):
                #    break 
                
                return t, frames

            else :
                time.sleep(0.2)
                #print("No frame")
                continue
        
    def findFace(self,gray_frame,frame):
        """
        It finds face and makes a rectangle on detected object

        Args:
            gray_frame : Gray scale image
            frame : Frame image
        """
        t_start = time.time()
        face = self.cascadeFile.detectMultiScale(gray_frame)

        for (a,b,c,d) in face:
            cv2.rectangle(frame, (a,b), (a+c,b+d), (255,255,255), 3)

        #cv2.imwrite("./images/{}.jpg".format(self.count),frame)
        self.count += 1
        #cv2.imshow("Detected Face", frame)
        #cv2.waitKey(1500)
        #cv2.destroyWindow("Detected Face")
        t_time = time.time()-t_start
        #print("Time Consumed ", (time.time()-t_start))
        return t_time, frame

objectDetection = Detection()

def videoStream():
    '''
    It shows frame in Label
    '''

    #ret,frame = cap.read()
    t, frame = objectDetection.detectFrame()

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
    import home.py

#creating tkinter instance
top = Tk()
top.geometry("1080x720")
top.resizable(width=False, height=False)

#creating canvas
canvas= Canvas(top,bg="#2B2B28", height=1500, width=1500)
canvas.pack()

#label
labelName = Label(top, text= "Face Detection Feed", width=18, background="#2B2B28", fg="White")
labelName.place(x=500,y=40)

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

