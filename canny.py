import cv2 as cv

path ="img\\"
src = cv.imread(path + "goksel.jpg")
h, w = src.shape[:2]
result = cv.resize(src, (w // 2, h // 2))
cv.imshow("result", result)
cv.waitKey(1000)

edge = cv.Canny(result, 10, 150)
h, w = src.shape[:2]
result = cv.resize(edge, (w // 2, h // 2))
cv.imshow("result", result)
cv.waitKey(1000)


