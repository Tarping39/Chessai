import cv2
img = cv2.imread("WIN_20220218_16_09_57_Pro.jpg")
crop_img = img[0:1072, 390:1540]
cv2.imwrite("WIN_01.jpg",crop_img)
#cv2.imshow("cropped", crop_img)
#cv2.waitKey(0)