import cv2
import numpy as np

#declare canny as image
def canny(image):
    #run the image to grayscale mode
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    #add the gausian blur to smoth the image and reduce the noisy using 5x5 kernel is good one
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    #apply canny canny detection on my smooth image to reduce the noise using treshold
    canny = cv2.Canny(blur, 50, 150)
    #we back to canny method again
    return canny

#read the image from left window
image = cv2.imread('test_image.jpg')
#analize the image using numpy
lane_image = np.copy(image)
#apply canny detect on 'test image.jpg'
canny = canny(lane_image)

#show the image as grayscale
cv2.imshow('result', canny)
#the image in form gray scale will appear "..." in mili second "0" is unlimited
cv2.waitKey(0)
#show the image in matrix
