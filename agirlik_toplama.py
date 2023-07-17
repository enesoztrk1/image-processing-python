import cv2

# reading the image
img = cv2.imread("photo.jpg")

# find row and column values
col,rows,a = img.shape

cv2.resize(img,(int(col/3),int(rows/3)))
cv2.namedWindow("Display window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Display window",img)


gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.resize(img,(int(col/3),int(rows/3)))
cv2.namedWindow("Result window",cv2.WINDOW_AUTOSIZE)
cv2.imshow("Result window",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()

