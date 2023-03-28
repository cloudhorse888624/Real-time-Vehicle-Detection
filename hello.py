import cv2
import numpy as np
import vehicles
import time

cap=cv2.VideoCapture("sap.mp4")

w=cap.get(3)
h=cap.get(4)
frameArea=h*w
areaTH=frameArea/900
kernalOp = np.ones((3, 3),np.uint8)
kernalOp2 = np.ones((5,5),np.uint8)
kernalCl = np.ones((11,11),np.uint)
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)
while(cap.isOpened()):
    ret, frame=cap.read()
    fgmask=fgbg.apply(frame)
    fgmask2=fgbg.apply(frame)
    if ret==True:
        ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
        ret,imBin2=cv2.threshold(fgmask2,200,255,cv2.THRESH_BINARY)
        mask=cv2.morphologyEx(imBin,cv2.MORPH_OPEN,kernalOp)
        mask=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,np.float32(kernalCl))
        countours0,hierarchy=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        for cnt in countours0:
            area=cv2.contourArea(cnt)   
            if area>areaTH:
                m=cv2.moments(cnt)
                cx=int(m['m10']/m['m00'])
                cy=int(m['m01']/m['m00'])
                x,y,w,h=cv2.boundingRect(cnt)
                cv2.circle(frame,(cx,cy),10,(0,0,255),-1)
                img=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.imshow('joe', img)     
        if cv2.waitKey(1)==ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
