
import cv

 #Point to where all our Haar stuff is 
harr_Cascade_Path = "/Users/Viv/Downloads/OpenCV-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml"
CAMERA_INDEX = 0

"""
Our only function, given an image detects images and returns their coordinates
"""
def findFaces(image):
    foundFaces = []
    # The following is called as recommended, will get rid of magic  numbers
    detected = cv.HaarDetectObjects(image, cascade, storage, 1.2, 2, cv.CV_HAAR_DO_CANNY_PRUNING, (100,100))
    if detected: # Yay it can find multiple faces!
        for (x,y,w,h),n in detected:
            foundFaces.append((x,y,w,h))
    return foundFaces
 
if __name__ == "__main__":
    cv.NamedWindow("Video", cv.CV_WINDOW_AUTOSIZE) # Make our window
 
    capture = cv.CaptureFromCAM(CAMERA_INDEX) #See what the camera sees
    storage = cv.CreateMemStorage() # Make room for it
    cascade = cv.Load(harr_Cascade_Path ) # See what we are looking for
    faces = []
 
    i = 0
    while True:
        image = cv.QueryFrame(capture) # Pick up the image
 
        # Only run the Detection algorithm every 5 frames to improve performance
        if i%5==0:
            faces = findFaces(image)
 
        for (x,y,w,h) in faces:
            cv.Rectangle(image, (x,y), (x+w,y+h), 255)
 
        cv.ShowImage("w1", image)
        i += 1
