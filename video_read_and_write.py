import numpy as np
import cv2 as cv

capture = cv.VideoCapture("video\\Istanbul.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv.CAP_PROP_FRAME_COUNT)
fps = capture.get(cv.CAP_PROP_FPS)
print(height, width, count, fps)

out = cv.VideoWriter("video\\Istanbul_save.avi",
                     cv.VideoWriter_fourcc('D', 'I', 'V', 'X'), 15,
                     (np.int(width), np.int(height)), True
                     )

while True:
    ret, frame = capture.read()

    if ret is True:
        cv.imshow("video-input", frame)
        out.write(frame)
        c = cv.waitKey(5)
        if c == 27:
            break

    else:
        break

capture.release()
out.release()
