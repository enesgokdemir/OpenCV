import cv2 as cv

path = "img\\"
src = cv.imread(path+"resim.jpg")

h, w = src.shape[:2]

img = src.copy()

roi = img[300:750, 950:1200, :]

roi.shape[:2]

cv.imshow("roi", roi)
cv.waitKey(1000)

roi = img[0:450, 0:350, :]

cv.imshow("img", img)
cv.waitKey(1000)

res = cv.resize(roi, None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(1000)

cv.destroyAllWindows()

