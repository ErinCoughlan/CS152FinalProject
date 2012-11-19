# Erin and Vivian's Final Projec
# Facial Emotion Identifcation
# CS 152 - Neural Networks

# Image Parsing

from getAllFiles import *
from constants import *

fileList = getAllFiles("/all_images");

total = 0;
finalFileList = [];
nFiles =len(fileList);
for i in range(nFiles):
    filename = fileList[i];
    
    # split the filenames to get emotions and to compare
    # example:
    # string = 'name_dir_emotion_open.pgm';
    # arr = ['name' 'dir' 'emotion' 'open' 'pgm'];
    arr = filename.split("_");
    
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
        finalFileList += filename;
        total = total + 1;

print "total: ", total;

#face = imread(fileName);
#imshow(face);
    
    

