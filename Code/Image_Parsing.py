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

    f = open(filename, "r")
    a = []
    foundData = False

    count = 0
    while True:
        line = f.readline()
        if not line:
            break
        elif "data" in line:
            foundData = True
        elif foundData:
            count += 1
            a.append(line.rstrip())
        elif ("data" in line) and foundData:
            line.replace("</data></name>", "")
            a.append(line.rstrip())
            foundData = False

    ans = []
    for i in range(len(a)):
        arr = a[0].split(" ")
        for j in range(len(arr)):
            char = arr[j]
            if char != '':
                ans.append(int(char))

    return ans


if __name__=="__main__":

  #  currDir, fileList = getAllFiles("/all_images")

 #   finalFileList = hot(fileList)

    currDir, fileList = getAllFiles("/xml")
    finalFileList = hot(fileList)
 #   finalFileList = [['A.xml', [0,0,1,0]]]

    num_samples = len(finalFileList)

    ans = []
    for filename, hotCode in finalFileList:
        fileArr = read_xml(filename)
        hotArr = [hotCode.index(1)]
        ans.append(fileArr + hotArr)

    final = np.array(ans)
    np.savetxt('data.txt', final, fmt='%10.f')
 

    # Sample data sets for testing
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
    
    # fmt determine format numbers should be in
    np.savetxt('test.txt', x, fmt='%10.5f')

##    # To read info back using numpy
##    new_data = np.loadtxt('test.txt')
##    new_data = new_data.reshape((4,5))

