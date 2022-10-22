import numpy as np
import cv2 as cv

path = "img\\"

img1 = cv.imread(path+"left.jpg")
img2 = cv.imread(path+"right.jpg")
cv.imshow("img1", img1)
cv.waitKey(1000)
cv.imshow("img2", img2)
cv.waitKey(1000)

horizontal = np.hstack((img1, img2))
cv.imshow("spider_man", horizontal)
cv.waitKey(3000)
cv.destroyAllWindows()
