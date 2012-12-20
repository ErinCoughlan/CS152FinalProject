import cv

imcolor = cv.LoadImage('vwehner.jpeg')
image = cv.LoadImage('vwehner.jpeg',cv.CV_LOAD_IMAGE_GRAYSCALE)

cornerMap = cv.CreateImage(cv.GetSize(imcolor), 8, 1)
cv.Canny(image, cornerMap, 50, 200)

for y in range(0, image.height):
    for x in range(0, image.width):
        canny = cv.Get2D(cornerMap, y, x) # get the x,y value
        # check the corner detector response
        if canny[0] > 10e-06:
            # draw a small circle on the original image
            cv.Circle(imcolor,(x,y),2,cv.RGB(155, 0, 25))

cv.NamedWindow('Canny', cv.CV_WINDOW_AUTOSIZE)
cv.ShowImage('Canny', imcolor) # show the image
cv.SaveImage('canny.jpg', imcolor)


def canny(im, (offX, offY)):
    features = []

    im = cv.CreateImage(cv.GetSize(im), 8, 1)
    cornerMap = cv.CreateImage(cv.GetSize(im), 8, 1)
    # OpenCV corner detection
    cv.Canny(im,cornerMap,50,200)

    dots = []
    for y in range(0, im.height):
        for x in range(0, im.width):
            canny = cv.Get2D(cornerMap, y, x) # get the x,y value
            # check the corner detector response
            if canny[0] > 10e-06:
                newX = x + offX
                newY = y + offY
                dots.append((newX, newY))

    features.append(dots)
    return features
