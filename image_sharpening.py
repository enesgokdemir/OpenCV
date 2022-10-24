import cv2 as cv
import numpy as np

path = "img\\"
src = cv.imread(path+"work.png")

sharpen_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

sharpen_image = cv.filter2D(src, cv.CV_32F, sharpen_op)

sharpen_image = cv.convertScaleAbs(sharpen_image)

cv.imshow("sharpen_image", sharpen_image)
cv.waitKey(1000)