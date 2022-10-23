import cv2 as cv

def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow("binary", binary)
    return binary


def canny_demo(image):
    t = 100
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow("canny_output", canny_output)
    return canny_output

path ="img\\"
src = cv.imread(path + "goksel.jpg")
h, w = src.shape[:2]
result = cv.resize(src, (w // 2, h // 2))
cv.imshow("result", result)
cv.waitKey(1000)

binary = threshold_demo(result)
canny = canny_demo(result)

contours, hierarchy = cv.findContours(canny, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

for c in range(len(contours)):
    cv.drawContours(result, contours, c, (0, 0, 255), 2, 8)

cv.imshow("contours-demo", result)
cv.waitKey(1000)

