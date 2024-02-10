import cv2


# img = cv2.imread("cv2/img&vid/cat.jpg")
# cv2.imshow("nhfgh", img)
#
# cv2.waitKey(5000)

img1 = cv2.imread("img&vid/face.JPG")
img1 = cv2.resize(img1, (img1.shape[1], img1.shape[0]))
# img1 = cv2.GaussianBlur(img1, (15, 15), 0)
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
img1 = cv2.Canny(img1, 35, 35)

cv2.imshow("nhfgh", img1)

cv2.waitKey(0)

