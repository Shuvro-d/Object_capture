import numpy as np
import cv2


def detect_object(image):
    areaArray = []
    lower = np.array([1, 1, 1])
    higher = np.array([255, 255, 255])

    count = 1

    no = 1
    res = image
    image = cv2.cvtColor(res, cv2.COLOR_BGR2RGB)
    mask2 = cv2.inRange(image, lower, higher)
    cont, _ = cv2.findContours(mask2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for i, c in enumerate(cont):
        area = cv2.contourArea(c)
        areaArray.append(area)
    sorteddata = sorted(zip(areaArray, cont), key=lambda x: x[0], reverse=True)

    cont_img = cv2.drawContours(image, cont, -1, (0, 0, 0), 3)

    c1 = sorteddata[0][1]  # largest
    c2 = sorteddata[1][1]
    x1, y1, w1, h1 = cv2.boundingRect(c1)
    x2, y2, w2, h2 = cv2.boundingRect(c2)
    cv2.drawContours(image, c1, -1, (0, 0, 0), 2)
    cv2.drawContours(image, c2, -1, (0, 0, 0), 2)
    cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 0), 2)
    cv2.rectangle(image, (x2, y2), (x2 + w2, y2 + h2), (0, 0, 0), 2)
    k1 = image[y1:y1 + h1, x1:x1 + w1]
    k2 = image[y2:y2 + h2, x2:x2 + w2]
    k1 = cv2.resize(k1, (640, 640))
    k2 = cv2.resize(k2, (640, 640))
    l=len(sorteddata)
    for i in range(l):
        if i>=5:
            break
        c = sorteddata[i][1]
        x1, y1, w1, h1 = cv2.boundingRect(c)
        cv2.drawContours(image, c, -1, (0, 0, 0), 2)
        cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (0, 0, 0), 2)
        k = image[y1:y1 + h1, x1:x1 + w1]
        k = cv2.resize(k, (640, 640))
        cv2.imshow(f"image {i}", k)
        cv2.waitKey(0)


image=cv2.imread("3.jpg")
detect_object(image)