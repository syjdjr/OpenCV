import cv2
import numpy as np

img = cv2.imread("python hw1_3.py board2.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 255)
_, dst = cv2.threshold(edges, 50, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

result = cv2.cvtColor(dst, cv2.COLOR_GRAY2BGR)

# 외곽선 검출
contours, hierarchy = cv2.findContours(dst, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

#근사
approx = cv2.approxPolyDP(contours[0], 0.02 * cv2.arcLength(contours[0], True), True)

rightbottom = approx[0]
leftbottom= approx[1]
lefttop=approx[2]
righttop = approx[3]

before= np.float32([lefttop, righttop, rightbottom, leftbottom])
after = np.float32([[0,500], [500,500],[500,0], [0,0]])


matrix = cv2.getPerspectiveTransform(before,after)
dst = cv2.warpPerspective(img,matrix,(500,500))
cv2.imshow('dst',dst)

        

# 출력
cv2.waitKey(0)
cv2.destroyAllWindows()
