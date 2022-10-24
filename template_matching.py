import cv2 as cv
import numpy as np

path = "img\\"
src = cv.imread(path+"humans.jpg")

def template_demo():
    src = cv.imread(path+"humans.jpg")
    tpl = cv.imread(path+"humans1.jpg")

    cv.imshow("input", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, tpl, method=cv.TM_CCORR_NORMED)
    cv.imshow("result", result)

    t = 0.98
    loc = np.where(result > t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)

    cv.imshow("demo", src)


template_demo()
cv.waitKey(10000)


