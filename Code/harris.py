import cv

imcolor = cv.LoadImage('vwehner.jpeg')
image = cv.LoadImage('vwehner.jpeg',cv.CV_LOAD_IMAGE_GRAYSCALE)
cornerMap = cv.CreateMat(image.height, image.width, cv.CV_32FC1)
# OpenCV corner detection
cv.CornerHarris(image,cornerMap,3)

for y in range(0, image.height):
 for x in range(0, image.width):
  harris = cv.Get2D(cornerMap, y, x) # get the x,y value
  # check the corner detector response
  if harris[0] > 10e-06:
   # draw a small circle on the original image
   cv.Circle(imcolor,(x,y),2,cv.RGB(155, 0, 25))

cv.NamedWindow('Harris', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Harris', imcolor) # show the image
cv.SaveImage('harris.jpg', imcolor)

def harris(im, (offX,offY)):
    features = []

    im = cv.CreateImage(cv.GetSize(im), 8, 1)
    cornerMap = cv.CreateMat(im.height, im.width, cv.CV_32FC1)
    # OpenCV corner detection
    cv.CornerHarris(im,cornerMap,3)

    dots = []
    for y in range(0, im.height):
        for x in range(0, im.width):
            harris = cv.Get2D(cornerMap, y, x) # get the x,y value
            # check the corner detector response
            if harris[0] > 10e-06:
                newX = x + offX
                newY = y + offY
                dots.append((newX, newY))

    features.append(dots)
    return features
    
