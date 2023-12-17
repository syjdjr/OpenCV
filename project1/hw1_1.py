import cv2
import numpy as np

img = cv2.imread("python hw1_1.py board2.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 50, 150)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=5)

if lines is not None:
    vertical_lines = 0
    horizontal_lines = 0
    
    for line in lines:
        x1, y1, x2, y2 = line[0]
        if abs(x2 - x1) > abs(y2 - y1):
            horizontal_lines += 1
        else:
            vertical_lines += 1

    if horizontal_lines < 12:
        print("8x8")
    
    else:
        print("10x10")

cv2.waitKey(0)
cv2.destroyAllWindows()
