import cv2
import numpy as np
import csv
from matplotlib import pyplot as plt

def cellPixelsConvexHull(_str):
    img = cv2.imread(_str)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    high_thresh, thresh_im = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    upper_thresh = np.mean(gray)

    _,contours,hierarchy = cv2.findContours(thresh_im, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    hull = []

    # calculate points for each contour
    for i in range(len(contours)):
        # creating convex hull object for each contour
        hull.append(cv2.convexHull(contours[i], False))

    # create an empty black image
    drawing = np.zeros((thresh_im.shape[0], thresh_im.shape[1], 3), np.uint8)

    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 0, 255) # green - color for contours
        color = (255, 255, 255) # blue - color for convex hull
        # draw ith contour
        cv2.drawContours(drawing, contours, i, color_contours, 1, 8, hierarchy)
        # draw ith convex hull object
        cv2.drawContours(drawing, hull, i, color, 1, 8)
    # save image for debugging purposes
    cv2.imwrite("convexHull_" + _str, drawing)
    cv2.drawContours(drawing, hull, -1, (255,255,255), thickness=-1)
    gray_d = cv2.cvtColor(drawing, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("convexHullFilled_" + _str, drawing)
    num_cells = cv2.countNonZero(gray_d)

    return num_cells

def calculatePixels(_str):
    # calculate activated (red) pixels
    img = cv2.imread(_str)
    ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
    gray = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)
    num_activated = cv2.countNonZero(gray)

    # calculate cell pixels
    num_cells = cellPixelsConvexHull(_str)

    # save image for debugging purposes
    # cv2.imwrite("converted_" + _str, thresh_im)

    # return pixel numbers
    return (num_activated, num_cells)

with open('taylor_lab_data2.csv', 'w') as csvfile:
    fieldnames = ['file_name', 'num_activated_pixels', 'num_cell_pixels', 'ratio', 'correctedCell_per_pixel']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (0,50):
        _str = ''
        if i < 10:
            _str += "IMAGE_00" + str(i) + ".tif"
        else:
            _str += "IMAGE_0" + str(i) + ".tif"

        (num_activated, num_cells) = calculatePixels(_str)
        ratio = float(num_activated)/num_cells*100
        correctedCell_per_pixel = ratio / 57.83 * 100
        writer.writerow({'file_name': _str, 'num_activated_pixels': num_activated, 'num_cell_pixels': num_cells, 'ratio': ratio,
        'correctedCell_per_pixel': correctedCell_per_pixel})

'''
# visualization
titles = ['Original Image','BINARY','GRAY']
images = [img, thresh1, gray]
for i in xrange(3):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
'''
