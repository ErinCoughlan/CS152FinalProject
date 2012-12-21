//  Recent authors, Erin Coughlan and Vivian Wehner
//       Seed canny code by Redjan F. Shabani


// Might need to redirect things

// My code
// export PKG_CONFIG_PATH=/Users/Viv/Documents/OpenCV-2.4.0/release/unix-install
// g++ canny.c `pkg-config --cflags --libs opencv`

// search for opencv.pc
// then export PKG_CONFIG_PATH=whereEverYouFound it

// To run, g++ canny.c `pkg-config --cflags --libs opencv`
// then ./a.out filename.jpg
//
// for our test files,
// ./a.out Neural/CS152FinalProject/Code/all_images/an2i_straight_happy_open.pgm

// Differences between cvMat, Mat and IpImage
// C++ Mat
// old intel is IpImage

#include <cv.h>
#include <stdio.h>
#include <stdlib.h>
#include <opencv/cxcore.h>
#include <iostream>
#include <string>
#include <opencv/highgui.h>
#define CV_IMWRITE_PXM_BINARY 32

using namespace cv;
using namespace std;

char* get_filename_from_path(char* filepath, int MAX_STR_LENGTH );
// Create a string that contains the exact cascade name
//const char* cascade_name ="/Users/Viv/Documents/OpenCV-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml";
const char* cascade_name ="/Users/ErinCoughlan/Desktop/OpenCV-2.4.0/data/haarcascades/haarcascade_frontalface_default.xml";

IplImage* detect_and_draw(IplImage *img);

int main(int argc,char** argv)
{
  Mat image;
  int MAX_STR_LENGTH = strlen(argv[1]);
  char* fileNameC = argv[1];
  string fileNameS = argv[1];

  image = cvLoadImage(argv[1]);

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

  IplImage * dummy = detect_and_draw(frameRG);
  cvShowImage("Dummy chance",dummy);

  // How big is it?
  CvSize sz2=cvGetSize(dummy);
  sz2.width=sz2.width;
  sz2.height=sz2.height;
  IplImage* realDummy=cvCreateImage(sz2,IPL_DEPTH_8U,0);

  cvCanny(dummy, realDummy, 40, 90, 3);
  cvShowImage("Original View",realDummy);
  cvShowImage("Canny Edges",framec);

  CvMat stub, *imgMat;
  imgMat = cvGetMat(realDummy, &stub, 0 , 0);

  // Output as a bmp
  //Mat img2Mat(framec);
  //if(!cvSaveImage("outFileName.bmp",framec))
    //if(!imwrite("outFileName.pbm",img2Mat))
    //printf("Could not save: %s\n","outFileName");

  char* result = get_filename_from_path(fileNameC, MAX_STR_LENGTH);

  int x;
  int newLen = strlen(result);
  int newStart = MAX_STR_LENGTH - newLen;
  char* tmp = result;

  for(x=0; x < newLen; x++){
    if ( x > newLen - 4){
      if(x == newLen - 3)
        tmp[x] = 'x';
      if(x == newLen - 2)
        tmp[x] = 'm';
      if (x == newLen - 1)
        tmp[x] = 'l';
    }
    else{
      if(fileNameC[newStart] == '_')
        tmp[x] = '0';
      else
        tmp[x] = fileNameC[newStart];
      newStart += 1;
    }
  }
  printf("with last char removed: %s\n",tmp);

  CvFileStorage* fs = cvOpenFileStorage(tmp, 0, CV_STORAGE_WRITE);
  cvSetIdentity (imgMat);
  cvWrite(fs, "bob", imgMat, cvAttrList(0,0));
  cvReleaseFileStorage( &fs);
  cvReleaseMat( &imgMat);

  // Will break on any key being hit
  //cvWaitKey(0);

}

char* get_filename_from_path(char* filepath, int MAX_STR_LENGTH ){
  char *filename = (char*)calloc(1, sizeof(MAX_STR_LENGTH));
  filename = (strrchr(filepath, '/')) + 1;
  printf(" found filename: %s\n", filename);
  return filename;

}


// Function to detect and draw any faces that is present in an image
IplImage* detect_and_draw( IplImage* img)
{
  static CvMemStorage* storage = 0;
  static CvHaarClassifierCascade* cascade = 0;
  int scale = 1;
  IplImage* temp = cvCreateImage( cvSize(img->width/scale,img->height/scale), 8, 3 );
  IplImage* dummy = cvCreateImage( cvSize(img->width/scale,img->height/scale), 8, 3 );

  // Create two points to represent the face locations
  CvPoint pt1, pt2;
  int i;

  cascade = (CvHaarClassifierCascade*)cvLoad( cascade_name, 0, 0, 0 );

  // Check whether the cascade has loaded successfully. Else report and error and quit
  if( !cascade )
    {
      fprintf( stderr, "ERROR: Could not load classifier cascade\n" );
      return temp;
    }

  // Allocate the memory storage
  storage = cvCreateMemStorage(0);

  // Create a new named window with title: result
  cvNamedWindow( "result", 1 );

  // Clear the memory storage which was used before
  cvClearMemStorage( storage );

  // Find whether the cascade is loaded, to find the faces. If yes, then:
  if( cascade )
    {

      // There can be more than one face in an image. So create a growable sequence of faces.
      // Detect the objects and store them in the sequence
      CvSeq* faces = cvHaarDetectObjects( img, cascade, storage,
                                          1.1, 2, CV_HAAR_DO_CANNY_PRUNING,
                                          cvSize(40, 40) );


      // Create a new rectangle for drawing the face
      CvRect* r = (CvRect*)cvGetSeqElem( faces, 0 );

      // Find the dimensions of the face,and scale it if necessary
      pt1.x = r->x*scale;
      pt2.x = (r->x+r->width)*scale;
      pt1.y = r->y*scale;
      pt2.y = (r->y+r->height)*scale;

      // Draw the rectangle in the input image
      cvRectangle( img, pt1, pt2, CV_RGB(255,0,0), 3, 8, 0 );

      /* sets the Region of Interest
         Note that the rectangle area has to be __INSIDE__ the image */
      cvSetImageROI(img, cvRect(r->x, r->y, r->width, r->height));

      /* create destination image
         Note that cvGetSize will return the width and the height of ROI */
      dummy = cvCreateImage(cvGetSize(img),
                                     img->depth,
                                     img->nChannels);

      /* copy subimage */
      cvCopy(img, dummy, NULL);
      /* always reset the Region of Interest */
      cvResetImageROI(img);


    }

  // Show the image in the window named "result"
  // cvShowImage( "result", img );
      cvShowImage("cropped", dummy);

  return dummy;

  // Release the temp image created.
  cvReleaseImage( &temp );

}