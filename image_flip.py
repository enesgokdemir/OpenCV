import numpy as np
import cv2 as cv

path = "img\\"
src = cv.imread(path+"resim.jpg")

# X Flip

dst1 = cv.flip(src, 0)
cv.imshow("x-flip", dst1)
cv.waitKey(1000)

# Y Flip

dst2 = cv.flip(src, 1)
cv.imshow("y-flip", dst2)
cv.waitKey(1000)

# XY Flip

dst3 = cv.flip(src, -1)
cv.imshow("xy-flip", dst3)
cv.waitKey(1000)

cv.destroyAllWindows()