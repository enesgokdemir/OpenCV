import cv2 as cv

path ="img\\"
src = cv.imread(path + "goksel.jpg")
h, w = src.shape[:2]
result = cv.resize(src, (w // 2, h // 2))
cv.imshow("result", result)
cv.waitKey(1000)

gray = cv.cvtColor(result, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("binary", binary)
cv.waitKey(1000)
cv.destroyAllWindows()