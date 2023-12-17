import cv2
import numpy as np

img = cv2.imread("python hw1_4.py board3.jpg", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(img, 100, 200)

blurred =cv2.blur(edges, (1,1))


circles = cv2.HoughCircles(blurred, cv2.HOUGH_GRADIENT, 1, 50, param1=150, param2=30, minRadius=5,maxRadius=45)


color = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

count=0
values=[]
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        cx, cy, radius = i
        #cv2.circle(color, (cx, cy), radius, (0, 0, 255), 2)
        #원 명암따라 구분
        mask = np.zeros_like(img)
        mask=cv2.circle(color, (cx, cy), radius, 2, 2)
        value = img[cy,cx]
        values.append(value)
        count +=1
        
bright_circle =0
average = np.average(values)
for value in values:
    if value > average:
        bright_circle +=1

print("w: %d b: %d" %( bright_circle, count-bright_circle))
cv2.waitKey(0)
cv2.destroyAllWindows()
