import cv2 as cv

path = "text\\"

model_bin = (path + "MobileNetSSD_deploy.caffemodel")
config_text = (path + "MobileNetSSD_deploy.prototxt")

objName = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog",
           "horse", "motorbike", "person", "sheep", "pottedplant", "sofa", "train",
           "tv", "monitor"]

net = cv.dnn.readNetFromCaffe(config_text, model_bin)

path1 = "img\\"
image = cv.imread(path1 + "dogs.jpg")
h = image.shape[0]
w = image.shape[1]

layerNames = net.getLayerNames()
lastLayerId = net.getLayerId(layerNames[-1])
lastLayer = net.getLayer(lastLayerId)

blobImage = cv.dnn.blobFromImage(image, 0.008444, (300, 300), (127.5, 127.5, 127.5), True, False)
net.setInput(blobImage)
cvOut = net.forward()

for detection in cvOut[0, 0, :, :]:
    score = float(detection[2])
    objIndex = int(detection[1])
    if score > 0.5:
        left = detection[3] * w
        top = detection[4] * h
        right = detection[5] * w
        bottom = detection[6] * h

        cv.rectangle(image, (int(left), int(top)), (int(right), int(bottom)), (255, 0, 0), thickness=2)
        cv.putText(image, "score: %2.f, %s" % (score, objName[objIndex]),
                   (int(left) - 10, int(top) - 5), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2, 8)


cv.imshow("mobile-ssd-demo", image)
cv.imwrite(path1 + "result.png", image)
cv.waitKey(1000)
