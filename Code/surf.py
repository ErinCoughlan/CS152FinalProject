import numpy as np
import cv2
import cv


imcolor = cv.LoadImage('vwehner.jpeg')
image = cv.LoadImage('vwehner.jpeg',cv.CV_LOAD_IMAGE_GRAYSCALE)

im = np.asarray(imcolor[:,:])
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

s = cv2.SURF();
mask = np.uint8(np.ones(gray.shape))
keypoints = s.detect(gray, mask)

dots = []
for point in keypoints:
    newX = int(point.pt[0])
    newY = int(point.pt[1])
    dots.append((newX,newY))

for point in dots:
    cv.Circle(imcolor,point,2,cv.RGB(155, 0, 25))

cv.NamedWindow('Surf', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Surf', imcolor) # show the image
cv.SaveImage('surf.jpg', imcolor)

def surf(im, (x,y)):
    features = []
    # correcting for data types
    # (must be numpy array for surf, but CvMat for draw)
    # actually need [:,:] it copies the image
    im = np.asarray(im[:,:])
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

    s = cv2.SURF();
    mask = np.uint8(np.ones(gray.shape))
    keypoints = s.detect(gray, mask)

    dots = []
    for point in keypoints:
        newX = int(point.pt[0]) + x
        newY = int(point.pt[1]) + y
        dots.append((newX,newY))

    features.append(dots)

    return features


