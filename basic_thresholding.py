import cv2 as cv

path = "img\\"
img = cv.imread(path+"work.png")

T = 127
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary" + str(i), binary)
cv.waitKey(10000)
cv.destroyAllWindows()