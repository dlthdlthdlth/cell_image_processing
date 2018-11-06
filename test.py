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
for i in range(len(contours)):v
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
# https://stackoverflow.com/questions/50450654/filling-in-circles-in-opencv
cv2.drawContours(drawing, hull, -1, (255,255,255), thickness=-1)

# convert the drawing to gray scaled image to count non-zeros
gray_d = cv2.cvtColor(drawing, cv2.COLOR_BGR2GRAY)
num_cells = cv2.countNonZero(gray_d)
print(num_cells)

# cv2.imshow("contours", drawing)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
