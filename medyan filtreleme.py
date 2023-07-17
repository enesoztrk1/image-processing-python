import cv2
import numpy as np

img = cv2.imread("photo.jpg")

median_blur = cv2.medianBlur(img,5)

cv2.namedWindow("Display window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Display window",img)

cv2.namedWindow("Result window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Result window",median_blur)
cv2.waitKey(0)
cv2.destroyAllWindows()