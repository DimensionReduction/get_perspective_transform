
import cv2
import numpy as np

def click(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDOWN:
        if len(pts)<4:
            pts.append([x,y])# 只记录前四次鼠标左击的位置
            cv2.circle(img,(x,y),1,(0,0,0))
            cv2.imshow('img1',img)
        else:
            cv2.destroyWindow('img1')# 第五次鼠标左击直接关闭图片窗口

img=cv2.imread('files.jpg')
pts=[]
cv2.namedWindow('img1')
cv2.setMouseCallback('img1',click)
cv2.imshow('img1',img)
cv2.waitKey(0)
pts.sort(reverse=False)
print(pts)
width,height=250,350
pts1=np.float32(pts)
pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
img2=cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow('img2',img2)
cv2.waitKey(0)