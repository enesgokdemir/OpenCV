import cv2 as cv

# HSV
path = "img\\"

img = cv.imread(path+"resim.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)
cv.waitKey(1000)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(1000)

cv.destroyAllWindows()