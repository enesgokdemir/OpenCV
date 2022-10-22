import numpy as np
import cv2 as cv

path = "img\\"

src = cv.imread(path+"resim.jpg", cv.IMREAD_GRAYSCALE)

# minMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %2.f, max_value: %2.f" % (min_value, max_value))
print("min_loc:", min_loc, "max_loc:", max_loc)

# meanStdDev

means, stddev = cv.meanStdDev(src)
print("mean: %2.f, stddev: %2.f" % (means, stddev))

src[np.where(src < means)] = 0
src[np.where(src > means)] = 255

cv.imshow("binary", src)
cv.waitKey(1000)

