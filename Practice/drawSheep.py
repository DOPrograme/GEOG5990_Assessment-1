# -*- coding: utf-8 -*-
"""
Created on Sun Apr 17 16:37:37 2022

@author: doujialiang
"""

import numpy as np
import os

import matplotlib.pyplot

import skimage.io 
from skimage import filters, color
import skimage.measure 

img = skimage.io.imread('sheep.png')
gray=color.rgb2gray(img) # 把它转换成灰度图像

thresh = filters.threshold_otsu(gray)
binary = gray <= thresh

#matplotlib.pyplot.imshow(binary, interpolation='nearest', cmap=matplotlib.pyplot.cm.gray) #灰灰的


# labels binary image
import skimage.morphology as mp
import skimage.measure as ms
binary=mp.binary_closing(binary,mp.diamond(1))
#binary=mp.binary_closing(binary,mp.diamond(1))
labels = ms.label(binary, neighbors=8)
contours = ms.find_contours(labels,0.2)

# Display the image and plot all contours found
with matplotlib.pyplot.xkcd():
    fig, ax = matplotlib.pyplot.subplots()
    ax.imshow(binary, interpolation='nearest', cmap=matplotlib.pyplot.cm.gray)
    
    for n, contour in enumerate(contours):
        ax.plot(contour[:, 1], contour[:, 0], linewidth=1)
    ax.annotate('Do you know?\n I\'m a cute sheep.', (0.2, 0.45), textcoords='axes fraction', size=20)
    
    ax.axis('image')
    ax.set_xticks([])
    ax.set_yticks([])
    matplotlib.pyplot.show()
