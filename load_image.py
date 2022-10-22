import cv2 as cv
img = cv.imread("resim.jpg")
type(img)
# namedWindow
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)
# imshow
cv.imshow("opencv_test", img)
cv.waitKey(1000)
cv.destroyAllWindows()


