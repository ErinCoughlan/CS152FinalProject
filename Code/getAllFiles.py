# Erin and Vivian's Final Projec
# Facial Emotion Identifcation
# CS 152 - Neural Networks

import os, sys

"""
getAllFiles:
    Retrieves the list of files in current directory
    Assumes that the top level folder is in current directory
    
    Input type: String(ext)
    Return type: String(currDir), [String(filenames)]
"""
def getAllFiles(ext):
    currDir = os.getcwd();
    currDir += ext;
    filenames = os.listdir(currDir);
    filenames.pop(0) # to get rid of the github hidden file
    return currDir, filenames;
