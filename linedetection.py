import cv2
import numpy as np

#read the image from left window
image = cv2.imread('test_image.jpg')
#analize the image using numpy
lane_image = np.copy(image)
#run the image to grayscale mode
gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
#show the image as grayscale
cv2.imshow('result', gray)
#the image in form gray scale will appear "..." in mili second "0" is unlimited
cv2.waitKey(0)
#show the image in matrix
