# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:31:49 2021

@author: G525459
"""
import numpy as np
import cv2
def get_grayscale(image):
    """Function that defines grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# noise removal
def remove_noise(image):
    """Function that removes noise"""
    return cv2.medianBlur(image,5)
 

def thresholding(image):
    """Simple Thresholding For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value."""
    # global thresholding just tresh binary
    return cv2.threshold(image,0, 255,  cv2.THRESH_BINARY +cv2.THRESH_OTSU)

#dilation
"""
make caracter bold
Dilation
This operations consists of convolving an image A with some kernel ( B), which can have any shape or size, usually a square or circle.
The kernel B has a defined anchor point, usually being the center of the kernel.
As the kernel B is scanned over the image, we compute the maximal pixel value overlapped by B and replace the image pixel in the anchor point position with that maximal value. As you can deduce, this maximizing operation causes bright regions within an image to "grow" (therefore the name dilation).
The dilatation operation is: dst(x,y)=max(x′,y′):element(x′,y′)≠0src(x+x′,y+y′)
Take the above image as an example. Applying dilation we can get:
"""
def dilate(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.dilate(image, kernel, iterations = 1)
    
#erosion inverse of dilation
def erode(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.erode(image, kernel, iterations = 1)

#opening - erosion followed by dilation
#Opening is just another name of erosion followed by dilation. It is useful in removing noise, 
#as we explained above. Here we use the function, cv.morphologyEx()
#closing Closing is reverse of Opening, Dilation followed by Erosion. 
#It is useful in closing small holes inside the foreground objects, or small black points on the object.
def opening(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#canny edge detection
def canny(image):
    return cv2.Canny(image, 100, 200)

#skew correction
def deskew(image):
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    return rotated

#template matching
#Template Matching is a method for searching and finding the location of a template image in a larger image. 
#OpenCV comes with a function cv.matchTemplate()
def match_template(image, template):
    return cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED) 