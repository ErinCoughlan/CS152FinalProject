
import cv
import cv2
import os, sys
import numpy as np
import scipy as sp

from surf import *
from harris import *
from canny import *

# constants
CAMERA_INDEX = 0
user = "erin" # user names are erin or viv

class FaceDetect:

    def __init__(self):
        """
            constructor for the FaceDetect class -- holds all the set-up needed
            for the detecting faces and recognizing features
        """

        #Point to where all our Haar stuff is (depends on the user)
        if user == "erin":
            harr_Cascade_Path = "/Users/ErinCoughlan/Desktop/OpenCV-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml"
        elif user == "viv":
            harr_Cascade_Path = "/Users/Viv/Downloads/OpenCV-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml"

        cv.NamedWindow("Video", cv.CV_WINDOW_AUTOSIZE) # Make our window

        self.capture = cv.CaptureFromCAM(CAMERA_INDEX) #See what the camera sees
        self.storage = cv.CreateMemStorage() # Make room for it
        self.cascade = cv.Load(harr_Cascade_Path) # See what we are looking for
        
        self.last_key_pressed = None

        self.faces = []
        self.faceFeatures = []
        self.faceFeatures2 = []
        self.faceFeatures3 = []


    def findFaces(self, image):
        """
            Given an image detects images and returns their coordinates
        """
        foundFaces = []
        # The following is called as recommended, will get rid of magic  numbers
        detected = cv.HaarDetectObjects(image, self.cascade, self.storage,
                                        1.2, 3, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
        if detected: # Yay it can find multiple faces!
            for (x,y,w,h),n in detected:
                foundFaces.append((x,y,w,h))

        self.faces = foundFaces


    def checkKeyPress(self, keyPressed):
        """ this method handles user key presses"""
        self.last_key_pressed = chr(keyPressed)

        # if a 'q' or Esc was pressed
        if keyPressed == ord('q') or keyPressed == 27: 
            cv.DestroyWindow("Video")
            sys.exit("Successful exit")
            


    def draw(self):
        """ draw everything on the screen, then show the image """
        for (x,y,w,h) in self.faces:
            cv.Rectangle(self.image, (x,y), (x+w,y+h), 255)

        for dots in self.faceFeatures:
           for point in dots:
               cv.Circle(self.image,point,2,cv.RGB(155, 0, 25))

        for dots in self.faceFeatures2:
           for point in dots:
               cv.Circle(self.image,point,2,cv.RGB(25, 0, 155))

        for dots in self.faceFeatures3:
           for point in dots:
               cv.Circle(self.image,point,2,cv.RGB(25, 155, 25))

        cv.ShowImage("Video", self.image)


    def handleNextImage(self):
        self.image = cv.QueryFrame(self.capture) # Pick up the image

        self.findFaces(self.image)

        self.findFeatures(self.image)

        self.draw()

        # To get input from the keyboard, we use cv.WaitKey
        # only the lowest eight bits matter (so we get rid of the rest):
        key_press_raw = cv.WaitKey(5) # gets a raw key press
        key_press = key_press_raw & 255 # sets all but the low 8 bits to 0
        # call a method to handle key presses (255 = "no key pressed")
        if key_press != 255:
            self.checkKeyPress(key_press)


    def findFeatures(self, image):
        features = []
        features2 = []
        features3 = []
        for (x,y,w,h) in self.faces:
            # extract the face
            copy = cv.CloneImage(image)
            subImg = cv.GetSubRect(copy, (x,y,w,h))

            offset = (x,y)
            features = surf(subImg, offset)
            features2 = harris(subImg, offset)
            features3 = canny(subImg, offset)
            

        self.faceFeatures = features
        self.faceFeatures2 = features2
        self.faceFeatures3 = features3

            


if __name__ == "__main__":
 
    fd = FaceDetect()

    i = 0
    while True:
        if i%5 == 0:
            fd.handleNextImage()
        i += 1
 

