import cv2

img = cv2.imread("flower2.png")

hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.namedWindow("Display Window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Display window",img)

cv2.namedWindow("Result Window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Result Window",hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()