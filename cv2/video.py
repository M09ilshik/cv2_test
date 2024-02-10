import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# cap = cv2.resize(cap, (cap.shape[1] * 2, cap.shape[0] * 2))


while True:

    success, img = cap.read()
    cv2.imshow("Video", img)
    # img = cv2.GaussianBlur(img, (15, 15), 0)
    r = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
    cv2.imshow("Video2", r)

    g = cv2.cvtColor(img, cv2.COLOR_YCrCb2BGR)
    cv2.imshow("Video3", g)

    b = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    b = cv2.Canny(b, 100, 100)
    cv2.imshow("Video4", b)
    kernel = np.ones((3, 3), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)







    cv2.waitKey(13)


