import numpy as np
import cv2 as cv

path = "img\\"
src = cv.imread(path+"resim.jpg")

print(src.shape)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1000)

print(gray.shape)
print(gray)

gray = np.float32(gray)
print(gray)

# NORM_MINMAX

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %2.f, max_value: %2.f" % (min_value, max_value))
print("min_loc:", min_loc, "max_loc:", max_loc)

means, stddev = cv.meanStdDev(gray)
print("mean: %2.f, stddev: %2.f" % (means, stddev))

dst = np.zeros(gray.shape, dtype=np.float32)

cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)

print(dst)

print(np.uint8(dst*255))
means, stddev = cv.meanStdDev(np.uint8(dst*255))
print("mean: %2.f, stddev: %2.f" % (means, stddev))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1000)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %2.f, max_value: %2.f" % (min_value, max_value))
print("min_loc:", min_loc, "max_loc:", max_loc)
means, stddev = cv.meanStdDev(dst)
print("mean: %2.f, stddev: %2.f" % (means, stddev))


cv.imshow("NORM_MINMAX", np.uint8(dst*255))
cv.waitKey(1000)


# NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(1000)

# NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*100000000))
cv.waitKey(1000)

# NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2", np.uint8(dst*100000))
cv.waitKey(1000)

