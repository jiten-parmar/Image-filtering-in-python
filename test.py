import cv2
img = cv2.imread("Resources/image2.jpg")
crop_img = img[0:100, 0:100]
cv2.imshow("cropped", crop_img)
cv2.waitKey(0)