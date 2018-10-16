import cv2
import numpy as np
import csv
from matplotlib import pyplot as plt

with open('names.csv', 'w') as csvfile:
    fieldnames = ['file_name', 'num_activated_pixels']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range (0,50):
        _str = ''
        if i < 10:
            _str += "IMAGE_00" + str(i) + ".tif"
        else:
            _str += "IMAGE_0" + str(i) + ".tif"
        img = cv2.imread(_str)
        ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
        gray = cv2.cvtColor(thresh1, cv2.COLOR_BGR2GRAY)
        #num_pixels = gray.size
        num_nonzero = cv2.countNonZero(gray)
        #print("total number of pixels: " + str(num_pixels))
        writer.writerow({'file_name': _str, 'num_activated_pixels': num_nonzero})
        print("number of pixels for activated parts: " + str(num_nonzero))
    # print("percentage: " + str((num_nonzero/float(num_pixels))*100))






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
