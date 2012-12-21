# Erin Coughlan and Vivian Wehner
# Script for running C program on faces

import os

# get current directory
currDir = os.getcwd();
imageDir = os.getcwd();
imageDir += "/all_images";
fileList = os.listdir(imageDir);

# set package path
retvalue = os.system("PKG_CONFIG_PATH=/Users/ErinCoughlan/Desktop/OpenCV-2.4.0/unix-install")
print retvalue, "Successfully changed system paths"

# compile the code
retvalue = os.system("g++ canny.c `pkg-config --cflags --libs opencv`")
print retvalue, "Successfully compiled canny.c"

# add all the files
for filename in fileList:
    name = imageDir + "/" + filename
    if filename[0] != ".":
        command = "./a.out " + name
        retvalue = os.system(command)

    print filename
