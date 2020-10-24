import cv2
frame = cv2.imread("user_sized_contour.png")
# gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY)
# cv2.imwrite()
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
dst = cv2.dilate(frame, kernel)
cv2.imwrite("dilate.png",dst)