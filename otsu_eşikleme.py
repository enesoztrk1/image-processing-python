import cv2

# reading the image
img = cv2.imread("lena.jpg")

# convert image to gray
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thres = cv2.threshold(gray,100,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow("thres",thres)

cv2.waitKey(0)

cv2.destroyAllWindows()

