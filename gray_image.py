import cv2 as cv
path = "img\\"

img = cv.imread(path+"resim.jpg")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)
cv.waitKey(1000)

# cvtColor
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1000)

# imwrite

cv.imwrite(path+"gray.png", gray)
cv.destroyAllWindows()

# IMREAD_GRAYSCALE
img = cv.imread(path+"resim.jpg", cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img)
cv.waitKey(1000)