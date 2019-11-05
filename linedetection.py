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

def display_lines(image, lines):
    #using zeros_like will  appear the image in zero intensity
    line_image = np.zeros_like(image)
    #if it is not empty
    if lines is not None:
        #using looping for print array x1, x2, x3, x4
        for line in lines:
            #representate the image in matrix pixel
            print(line)

#define specific area we wnat to calculate in threshol mode
def region_of_interset(image):
    #the heightness of our image
    height = image.shape[0]
    #this is we get from the violet image we calculate the line in the line road
    polygons = np.array([
    [(200, height), (1100, height), (550, 250)]
    ])
    #make our image totally black that only have the triangle that following the line road
    mask = np.zeros_like(image)
    #our line is white
    cv2.fillPoly(mask, polygons, 255)
    #add bitwise operator in our image
    masked_image = cv2.bitwise_and(image, mask)
    #back to masked image again
    return masked_image

#read the image from left window
image = cv2.imread('test_image.jpg')
#analize the image using numpy
lane_image = np.copy(image)
#apply canny detect on 'test image.jpg'
canny = canny(lane_image)
croped_image = region_of_interset(canny)
#....
lines = cv2.HoughLinesP(croped_image, 2, np.pi/180, 100, np.array([]), minLineLength=40, maxLineGap=5)
#display the line in the image
line_image = display_lines(lane_image, lines)
#show the image as cv2
cv2.imshow("result", croped_image)
#the image in will display on the screen
cv2.waitKey(0)


