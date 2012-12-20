
import cv
import cv2
import os, sys
import numpy as np
import scipy as sp
from scipy.linalg import svd
from scipy.misc import lena
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

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
               cv.Circle(self.image, point, 1, 255)

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
        for (x,y,w,h) in self.faces:
            # extract the face
            copy = cv.CloneImage(image)
            img = cv.GetSubRect(copy, (x,y,w,h))
            subImg = cv.GetSubRect(copy, (x,y,w,h))
            
            # correcting for data types
            # (must be numpy array for surf, but CvMat for draw)
            # actually need [:,:] it copies the image
            subImg = np.asarray(subImg[:,:])
            gray = cv2.cvtColor(subImg, cv2.COLOR_BGR2GRAY)

            s = cv2.SURF();
            mask = np.uint8(np.ones(gray.shape))
            keypoints = s.detect(gray, mask)

            dots = []
            for point in keypoints:
                newX = int(point.pt[0]) + x
                newY = int(point.pt[1]) + y
                dots.append((newX,newY))

            #features.append(dots)

            t = np.arange(100)
            time = np.sin(0.1*t)
            real = time[:,np.newaxis,np.newaxis]*np.repeat(img[np.newaxis,...],100,axis=0)

            # we add some noise
            noisy = real + np.random.randn(*real.shape)*255

            # types*observations matrix
            M = noisy.reshape(noisy.shape[0],-1).T

            # singular value decomposition factorises your data matrix such that
            # 
            #   M = U*S*V.T     (where '*' is matrix multiplication)
            # 
            # U and V are the singular matrices, containing orthogonal vectors of
            # unit length in their rows and columns respectively. S is a diagonal
            # matrix containing the singular values of M - these values squared will
            # give the proportional variance explained by each PC. since U and V
            # both contain orthogonal vectors, U*V.T is a whitened version of M.
            U,s,Vt = svd(M,full_matrices=False)
            V = Vt.T

            # sort the PCs by descending order of the singular values (i.e. by the
            # proportion of total variance they explain)
            ind = np.argsort(s)[::-1]
            U = U[:,ind]
            s = s[ind]
            V = V[:,ind]

            # if we use all of the PCs we can reconstruct the noisy signal perfectly
            S = np.diag(s)
            Mhat = np.dot(U,np.dot(S,V.T))
            #print "Using all PCs, MSE = %.6G" %(np.mean((M-Mhat)**2))

            for i in range(0, len(Mhat[0])):
                dots.append((int(Mhat[0][i]), int(Mhat[1][i])))

            features.append(dots)
            
        self.faceFeatures = features

            


if __name__ == "__main__":
 
    fd = FaceDetect()

    while True:
        fd.handleNextImage()
 

