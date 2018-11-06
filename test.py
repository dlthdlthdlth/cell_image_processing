import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('IMAGE_041.tif')
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)

high_thresh, thresh_im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
# upper_thresh = np.mean(gray)
# high_thresh2, thresh_im2 = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)

# https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/
_,contours,hierarchy = cv2.findContours(thresh_im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
hull = []

# calculate points for each contour
for i in range(len(contours)):
    # creating convex hull object for each contour
    hull.append(cv2.convexHull(contours[i], False))

# create an empty black image
drawing = np.zeros((thresh_im.shape[0], thresh_im.shape[1], 3), np.uint8)

# draw contours and hull points:
for i in range(len(contours)):
    color_contours = (0, 255, 0) # green - color for contours
    color = (255, 0, 0) # blue - color for convex hull
    # draw ith contour
    cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
    # draw ith convex hull object
    cv2.drawContours(drawing, hull, i, color, 1, 8)

# https://www.learnopencv.com/convex-hull-using-opencv-in-python-and-c/ ends

# fill in the hull with white pixels
cv2.drawContours(drawing, hull, -1, (255,255,255), thickness=-1)

# convert the drawing to gray scaled image to count non-zeros
gray_d = cv2.cvtColor(drawing, cv2.COLOR_BGR2GRAY)
num_cells = cv2.countNonZero(gray_d)
print(num_cells)

# cv2.imshow("contours", drawing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




#filter = cv2.Canny(thresh_im,lowThresh, high_thresh)
# num_nonzero = cv2.countNonZero(thresh_im)

# (x,y),radius = cv2.minEnclosingCircle(cnt)
# center = (int(x),int(y))
# radius = int(radius)
# cv2.circle(img,center,radius,(0,255,0),2)
# get contours from image
# image, contours, hier = cv2.findContours(thresh_im, cv2.RETR_EXTERNAL,
#                     cv2.CHAIN_APPROX_SIMPLE)

# for each contour
# for cnt in contours:
#     # get convex hull
#     hull = cv2.convexHull(cnt)
#     # draw it in red color
#     cv2.drawContours(thresh_im, [hull], -1, (0, 0, 255), 1)




# contour stuff
# im2, contours, hierarchy = cv2.findContours(thresh_im,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cv2.drawContours(thresh_im,contours,-1,(0,255,0),3)
# num_nonzero = cv2.countNonZero(thresh_im)
# print(num_nonzero)

#print(num_nonzero)

# cv2.imshow('image', thresh_im)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.subplot(2,1,1), plt.imshow(filter)
# plt.subplot(2,1,2), plt.imshow(RGB_gray)
# plt.show()

# convolute with proper kernels
# laplacian = cv2.Laplacian(img,cv2.CV_64F)
# print(laplacian.shape)
# gray = cv2.cvtColor(laplacian, cv2.COLOR_BGR2GRAY)

#sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  # x
#sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)  # y
# print(sobelx.dtype)
# sobelx = cv2.cvtColor(sobelx, cv2.COLOR_BGR2GRAY)
#filter = cv2.Canny(sobelx,50,70)


# plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,3),plt.imshow(sobelx,cmap = 'gray')
# plt.title('Sobel X'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,2,4),plt.imshow(sobely,cmap = 'gray')
# plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])
#
# plt.show()
# plt.imshow('image', filter)
# plt.show()

# plt.subplot(2,1,1),plt.imshow(gray,cmap = 'gray')
# plt.title('Original'), plt.xticks([]), plt.yticks([])
# plt.subplot(2,1,2),plt.imshow(filter,cmap = 'gray')
# plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
# plt.show()

# plt.imshow(filter, cmap ='gray')
# plt.show()
