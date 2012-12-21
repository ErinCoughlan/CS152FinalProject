//  Recent authors, Erin Coughlan and Vivian Wehner
//       Seed code by Redjan F. Shabani


// To run, g++ canny.c `pkg-config --cflags --libs opencv`
// then ./a.out filename.jpg 

// Differences between cvMat, Mat and IpImage
// C++ Mat
// old intel is IpImage

#include "cv.h"
#include "stdio.h"
#include "cxcore.h"
#include <iostream>
#include <string>
#include "highgui.h"
#define CV_IMWRITE_PXM_BINARY 32

using namespace cv;
using namespace std;
void replace_char (char *s, char find, char replace);

int main(int argc,char** argv)
{
  Mat image;

  // Load a new image
  image = imread(argv[1], CV_LOAD_IMAGE_COLOR);

  // Check for invalid input
  if(! image.data ){
    cout <<  "Could not open or find the image" << std::endl ;
    return -1;
  }

  // Make a new window and display it
  namedWindow("CannyEdges", CV_WINDOW_AUTOSIZE);

  IplImage* frameRGB=cvCloneImage(&(IplImage)image);

  IplImage* frameG=cvCreateImage(cvGetSize(frameRGB),IPL_DEPTH_8U,0);
  cvConvertImage(frameRGB,frameG,0); 

  // How big is it? 
  CvSize sz=cvGetSize(frameRGB);
  sz.width=sz.width;
  sz.height=sz.height;
            
  // Another Frame! 
  IplImage* frameRG=cvCreateImage(sz,IPL_DEPTH_8U,0);
  cvResize(frameG, frameRG,CV_INTER_LINEAR);
            
  // Another Frame, the same size
  IplImage* framec=cvCreateImage(sz,IPL_DEPTH_8U,0);
            
  // Finally, run Canny on the RG frame and put it into the dummy frame
  // Takes in (Mat& image, Mat&)
  // 
  cvCanny(frameRG, framec, 40, 90, 3);

 
  cvShowImage("Original View",frameRGB);
  cvShowImage("Canny Edges",framec);
  
  CvMat stub, *imgMat;
  imgMat = cvGetMat(framec, &stub, 0 , 0);

  // Output as a bmp

  //Mat imgMat(framec);
  //if(!cvSaveImage("outFileName.bmp",framec))
  //if(!imwrite("outFileName.pbm",imgMat))
  //  printf("Could not save: %s\n","outFileName");
            
  printf ("%c", fileName);
  CvFileStorage* fs = cvOpenFileStorage( "example.xml" , 0, CV_STORAGE_WRITE);
  cvSetIdentity (imgMat);
  cvWrite(fs, "name", imgMat, cvAttrList(0,0));
  cvReleaseFileStorage( &fs);
  cvReleaseMat( &imgMat);

  // 33 second delay, will break on any key being hit
  cvWaitKey(0);

  return 0;
}

void replace_char (char *s, char find, char replace) {
  while (*s != 0) {
    if (*s == find)
      *s = replace;
    s++;
  }
}

