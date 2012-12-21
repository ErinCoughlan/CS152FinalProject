# Erin and Vivian's Final Projec
# Facial Emotion Identifcation
# CS 152 - Neural Networks

# Image Parsing

#from getAllFiles import *
from constants import *

import os, sys
import re

import cv
import numpy as np
import scipy
import matplotlib.pyplot as plt



def getAllFiles(ext):
    """
    Retrieves the list of files in current directory
    Assumes that the top level folder is in current directory
    
    Input type: String(ext)
    Return type: String(currDir), [String(filenames)]
    """

    currDir = os.getcwd();
    currDir += ext;
    filenames = os.listdir(currDir);
    filenames.pop(0) # to get rid of the github hidden file
    return currDir, filenames;



def hot(fileList):
    """
    Parses the files and returns a list of only relevant images and their
    hot codes.

    Input type: fileList
    Return type: fileList
    """

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
    print "first file and code: ", finalFileList[0]

    return finalFileList

def read_xml(filename):
    """ Return image data from an xml file as a numpy array. """

    return np.empty


if __name__=="__main__":

    currDir, fileList = getAllFiles("/all_images");

    finalFileList = hot(fileList)

    num_samples = len(finalFileList)

    arr = []
    for sample in range(num_samples):
        path = currDir + '/' + finalFileList[sample][0];
        hotCode = finalFileList[sample][1]
        
        face = cv.LoadImageM(path, cv.CV_LOAD_IMAGE_GRAYSCALE);
        a = np.asarray( face[:,:] )
        nRow, nCol = a.shape
        curr = []
        for row in range(nRow):
            for val in a[row]:
                curr.append(val)

        arr.append(curr)

##    # experiement on the first image
##    a = np.array(arr[0])
##    size = a.size
##    np.savetxt('first_face.txt', a)
##
##    # make the image come back
##    new_data = np.loadtxt('first_face.txt')
##    new_data = new_data.reshape((120,128))
##
##    plt.imshow(new_data) #Needs to be in row,col order
##    plt.savefig('haha.png')
 

    # Save data to a text file using numpy
    # classes as target
    x1 = [[1,0,0,0,0,2],[0,0,0,1,0,2],[1,0,0,0,0,1],[1,1,1,0,0,0],
         [0,1,0,0,0,1],[0,0,0,1,0,2],[1,0,0,0,1,3],[1,1,1,1,0,0],
         [0,0,0,0,0,1],[0,0,1,1,1,2],[1,0,0,1,0,1],[1,0,1,1,0,0],
         [1,0,0,0,1,3],[0,0,0,1,0,2],[1,0,0,0,0,1],[1,1,1,0,1,0],
         [1,0,0,0,1,3],[0,0,0,1,0,2],[1,0,0,0,0,1],[1,1,1,0,0,0]]

    # hot code array as target
    x2 = [[1,0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,1,0,0],[1,1,1,0,0,0,0,0,0],
         [0,1,0,0,0,0,1,0,0],[0,0,0,1,0,0,0,1,0],[1,0,0,0,1,0,0,0,1],[1,1,1,1,0,0,0,0,0],
         [0,0,0,0,0,0,1,0,0],[0,0,1,1,1,0,0,1,0],[1,0,0,1,0,0,1,0,0],[1,0,1,1,0,0,0,0,0],
         [1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,1,0,0],[1,1,1,0,1,0,0,0,0],
         [1,0,0,0,1,0,0,0,1],[0,0,0,1,0,0,0,1,0],[1,0,0,0,0,0,1,0,0],[1,1,1,0,0,0,0,0,0]]
    
    x = np.array(x1)
    print x
 #   x = np.arange(20).reshape((4,5))
    # fmt determine format numbers should be in
    np.savetxt('test.txt', x, fmt='%10.5f')
##
##    # To read info back using numpy
##    new_data = np.loadtxt('test.txt')
##    new_data = new_data.reshape((4,5))

