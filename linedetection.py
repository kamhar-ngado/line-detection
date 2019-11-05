import cv2
import numpy as np

def avarage_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2), 1)
        slope = parameters[0]
        intercept = parameters[1]
        if slope < 0:
            left_fit.append((slope, intercept))
        else:
            right_fit.append((slope, intercept))
        print(left_fit)
        print(right_fit)



# declare canny as image
def canny(image):
    # run the image to grayscale mode
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    # add the gausian blur to smoth the image and reduce the noisy using 5x5 kernel is good one
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    # apply canny canny detection on my smooth image to reduce the noise using treshold
    canny = cv2.Canny(blur, 50, 150)
    # we back to canny method again
    return canny


def display_lines(image, lines):
    # using zeros_like will  appear the image in zero intensity
    line_image = np.zeros_like(image)
    # if it is not empty
    if lines is not None:
        # using looping for print array x1, x2, x3, x4
        for line in lines:
            #rebulding our image
            x1, y1, x2, y2 = line.reshape(4)
            # change the line from 2D to 1D
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_image


# define specific area we wnat to calculate in threshol mode
def region_of_interset(image):
    # the heightness of our image
    height = image.shape[0]
    # this is we get from the violet image we calculate the line in the line road
    polygons = np.array([
        [(200, height), (1100, height), (550, 250)]
    ])
    # make our image totally black that only have the triangle that following the line road
    mask = np.zeros_like(image)
    # our line is white
    cv2.fillPoly(mask, polygons, 255)
    # add bitwise operator in our image
    masked_image = cv2.bitwise_and(image, mask)
    # back to masked image again
    return masked_image


# read the image from left window
image = cv2.imread('test_image.jpg')
# analyze the image using numpy
lane_image = np.copy(image)
# apply canny detect on 'test image.jpg'
canny_image = canny(lane_image)
croped_image = region_of_interset(canny_image)
# Apply hough transformation formula
lines = cv2.HoughLinesP(croped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
#..
avaraged_lines = avarage_slope_intercept(lane_image, lines)
# display the line in the image
line_image = display_lines(lane_image, lines)
# show the image as cv2
#combina original image with black hough transformation
combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
#display the combo image
cv2.imshow("result", combo_image)
# the image in will display on the screen
cv2.waitKey(0)
