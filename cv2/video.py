import cv2


cap = cv2.VideoCapture("img&vid/video.mp4")

while True:
    success, img = cap.read()
    cv2.imshow("Video", img)

    cv2.waitKey(10)