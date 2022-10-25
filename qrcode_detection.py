import cv2 as cv
import numpy as np

path = "img\\"
src = cv.imread(path+"qr_code.png")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

qr = cv.QRCodeDetector()

codeinfo, points, straight_qrcode = qr.detectAndDecode(gray)

print(points)

result = np.copy(src)

cv.drawContours(result, [np.int32(points)], 0, (0, 0, 255), 4)

print("qrcode information is:\n%s" % codeinfo)

cv.imshow("result", result)
cv.waitKey(1000)


