import cv2
import numpy as np

img = cv2.imread("python hw1_2.py board2.jpg")
count = 0

corner =[None, None, None, None] #corner None 으로 안채우면 type error 
def mouse(event,x,y,flags,param):
    global count
    if event == cv2.EVENT_LBUTTONDOWN:
        corner[count] = (x,y)
        count +=1
    
        if count == 4:
            lefttop = corner[0]
            righttop= corner[1]
            rightbottom=corner[2]
            leftbottom = corner[3]
            
            width = abs(righttop[0] - lefttop[0])
            height = abs(lefttop[1] - leftbottom[1])
            
            before= np.float32([lefttop, righttop, rightbottom, leftbottom])
            after = np.float32([[0,0], [width ,0],[width,height], [0,height]])
        
            matrix = cv2.getPerspectiveTransform(before,after)
            dst = cv2.warpPerspective(img,matrix,(width,height))
            cv2.imshow('dst',dst)
        
cv2.imshow('img',img)
cv2.setMouseCallback('img', mouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
