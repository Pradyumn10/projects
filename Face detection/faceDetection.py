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
from threading import Thread

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

                cv2.imshow("frame" ,frame)
                if cv2.waitKey(1) & 0xFF == ord(" "):
                    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                    self.findFace(gray_frame,frame)
                    #return gray_frame,frame
                if cv2.waitKey(1) &0xFF == ord("q"):
                    break 
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

        cv2.imwrite("./images/{}.jpg".format(self.count),frame)
        self.count += 1
        cv2.imshow("Detected Face", frame)
        cv2.waitKey(1500)
        cv2.destroyWindow("Detected Face")
        print("Time Consumed ", (time.time()-t_start))

#running the class
if __name__ == "__main__":
    run = Detection()
    run.detectFrame()
