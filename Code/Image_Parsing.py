# Erin and Vivian's Final Projec
# Facial Emotion Identifcation
# CS 152 - Neural Networks

# Image Parsing

from getAllFiles import *
from constants import *
import re

# OpenCV is super annoying
import cv

currDir, fileList = getAllFiles("/all_images");

total = 0;
finalFileList = [];
nFiles = len(fileList);
for i in range(nFiles):
    filename = fileList[i];
    
    # split filenames to get components
    arr = re.split(r"[_.]",filename);

    arrDir = arr[DIR];
    arrEmo = arr[EMOTION];
    arrOpen = arr[OPEN];
    
    success = False;
    # We only want to look at pictures that are straight on
    # and don't have glasses
    if 'straight' == arrDir and 'open' == arrOpen:
        # initialize hot code
        hotCode = [0,0,0,0];
        success = True;
        if 'angry' == arrEmo:
            hotCode[ANGRY] = 1;
        elif 'happy' == arrEmo:
            hotCode[HAPPY] = 1;
        elif 'neutral' == arrEmo:
            hotCode[NEUTRAL] = 1;
        elif 'sad' == arrEmo:
            hotCode[SAD] = 1;
        else:
            print 'No emotion data';
            success = False;
    
    if success:
        finalFileList.append([filename, hotCode]);
        total = total + 1;

print "total: ", total;

# display first image for testing
# get full path name
##index = 0;
##path = currDir + '/' + finalFileList[index][0];
##face = cv.LoadImage(path, cv.CV_LOAD_IMAGE_GRAYSCALE);
##windowTitle = "face: " + str(index);
##cv.ShowImage(windowTitle, face);

# wait for a keypress
#cv.WaitKey(0);
