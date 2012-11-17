

%% Load raw image file
image = imread('vwehner.jpeg');
%iptsetpref ImshowBorder tight
%imshow(image)

%% Crop region of interest
%%cropped = imcrop(face1, [120 0 580 300]);
%%imshow(cropped)

%% Segment by thresholding
%%thresh = 100;
%%altered = im2bw(cropped, thresh/255);
%%imshow(altered)

%% Tool to measure things in the image, delete after use if you want
%% d = imdistline; 

%% Make a gray scale image
thresh=150;
gray_orig = rgb2gray(image);
imshow(gray_orig);
gray_image = im2bw(gray_orig, thresh/255);
imshow(gray_image)
%% Finding circles
%%[centers, radii] = imfindcircles(circles, [38 45], 'objectPolarity', 'dark', 'Sensitivity',0.92)
%%viscircles(centers, radii)

%% Finding edges
%BW1 = edge(gray_image, 'sobel');
%BW2 = edge(gray_image, 'canny');
%imshow(BW2)
%figure, imshow(BW2)

%% Finding Corners
%subplot(1,2,1)
%corners = corner(gray_image);
%imshow(gray_image);
%hold on
%plot(corners(:,1),corners(:,2),'.', 'Color','g')
%hold off

%% Tracing Boundaries in an Image

BW = im2bw(gray_image);
imshow(BW)
dim = size(BW);
col = round(dim(2)/2)-90;
row = min(find(BW(:,col)));
boundary = bwtraceboundary(BW, [row,col], 'N');
imshow(gray_image)
hold on;
plot(boundary(:,2),boundary(:,1),'g','LineWidth', 3);
BW_filled = imfill(BW,'holes');
boundaries = bwboundaries(BW_filled);
for k=1:10
   b = boundaries{k};
   plot(b(:,2),b(:,1),'g','LineWidth',3);
end



