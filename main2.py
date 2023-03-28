## Graspcoding.com

import cv2
import numpy as np
import vehicles
import time
import csv
import collections
import numpy as np
import ultralytics
ultralytics.checks()
from ultralytics import YOLO
from PIL import Image

cnt_up=0
cnt_down=0
cnt_dl=0
cnt_ld=0
cnt_lr=0
cnt_rl=0
cnt_dr=0
cnt_rd=0

cap=cv2.VideoCapture("sap.mp4")

model = YOLO("./yolov8n.pt")
#Get width and height of video

w=cap.get(3)
h=cap.get(4)
frameArea=h*w
areaTH=frameArea/900

#Lines
line_up=int(1.9*(h/5))
line_down=int(3*(h/5))

up_limit=int(1*(h/5))
down_limit=int(4*(h/5))

print("Red line y:",str(line_down))
print("Blue line y:",str(line_up))
line_down_color=(255,0,0)
line_up_color=(255,0,255)
pt1 =  [116, 186]
pt2 =  [252, 197]
pts_L1 = np.array([pt1,pt2], np.int32)

pt3 =  [140, 160]
pt4 =  [207, 140]
pts_L2 = np.array([pt3,pt4], np.int32)


pt5 =  [248, 147]
pt6 =  [281, 154]
pts_L3 = np.array([pt5,pt6], np.int32)



#Background Subtractor
fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)

#Kernals
kernalOp = np.ones((3,3),np.uint8)
kernalOp2 = np.ones((5,5),np.uint8)
kernalCl = np.ones((11,11),np.uint)


font = cv2.FONT_HERSHEY_SIMPLEX
cars = []
max_p_age = 5
pid = 1

ii = True 
while(cap.isOpened()):
    ret, frame=cap.read()
    
    for i in cars:
        i.age_one()

    if ret==True:
        
        results = model.predict(source=frame, save=False)

        
        for output in results:

                position = output.boxes.xywh.tolist()
                print(position)
                ####Tracking######
                for i, pos in enumerate(position):
                                      
                    [x,y,w,h] = [int(pos[0]), int(pos[1]), int(pos[2]), int(pos[3])]
                    cx=x
                    cy=y
                new=True
              
                for i in cars:
                    if abs(x - i.getX()) <= 2*w and abs(y - i.getY()) <= 2*h:
                        new = False
                        i.updateCoords(cx, cy)
                        direction=i.which_way()
            
                        if i.lenDir()==2:
                            if direction==[1, 2]:
                                print(i.i)
                                cnt_dl+=1
                                
                            if direction==[1, 3]:
                                cnt_dr+=1
                                
                            if direction==[2, 1]:
                                cnt_ld+=1
                                
                            if direction==[3, 1]:
                                cnt_rd+=1
                                
                            if direction==[2, 3]:
                                cnt_lr+=1
                               
                            if direction==[3, 2]:
                                cnt_rl+=1
                               
                            if i.getState()=='2':
                                index=cars.index(i)
                                cars.pop(index)
                                del i
                        
                    
                        
                    
                    #         if i.going_UP(line_down,line_up)==True:
                    #             cnt_up+=1
                    #             print("ID:",i.getId(),'crossed going up at', time.strftime("%c"))
                    #         elif i.going_DOWN(line_down,line_up)==True:
                    #             cnt_down+=1
                    #             print("ID:", i.getId(), 'crossed going up at', time.strftime("%c"))
                    #         break
                    # if i.getState()=='1':
                    #         if i.getDir()=='down'and i.getY()>down_limit:
                    #             i.setDone()
                    #         elif i.getDir()=='up'and i.getY()<up_limit:
                    #             i.setDone()
                    # if i.timedOut():
                    #         index=cars.index(i)
                    #         cars.pop(index)
                    #         del i

                if new==True: #If nothing is detected,create new
                        p=vehicles.Car(pid,cx,cy,max_p_age, pts_L1, pts_L2, pts_L3)
                        cars.append(p)
                        pid+=1

                cv2.circle(frame,(cx,cy),5,(0,0,255),-1)
                img=cv2.rectangle(frame,(x-int(w/2),y-int(h/2)),(x+int(w/2),y+int(h/2)),(0,255,0),2)

        for i in cars:
            cv2.putText(frame, str(i.getId()), (i.getX(), i.getY()), font, 0.3, i.getRGB(), 1, cv2.LINE_AA)




        str_dl='DOWN->LEFT: '+str(cnt_dl)
        str_ld='LEFT->DOWN: '+str(cnt_ld)
        str_dr='DOWN->RIGHT: '+str(cnt_dr)
        str_rd='RIGHT->DOWN: '+str(cnt_rd)
        str_lr='LEFT->RIGHT: '+str(cnt_lr)
        str_rl='RIGHT->LEFT: '+str(cnt_rl)
        pts_l1 = np.array([[116, 186], [252, 197]], np.int32)
        pts_l1 = pts_l1.reshape((-1,1,2))
        pts_l2 = np.array([[140, 160], [207, 140]], np.int32)
        pts_l2 = pts_l2.reshape((-1,1,2))
        pts_l3 = np.array([[248, 147], [281, 154]], np.int32)
        pts_l3 = pts_l3.reshape((-1,1,2))
        frame=cv2.polylines(frame,[pts_l1],False,line_down_color,thickness=2)
        frame=cv2.polylines(frame,[pts_l2],False,line_up_color,thickness=2)
        frame=cv2.polylines(frame,[pts_l3],False,(0,255,0),thickness=1)
        
        cv2.putText(frame, str_dl, (10, 40), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_dl, (10, 40), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, str_ld, (10, 70), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_ld, (10, 70), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, str_dr, (10, 100), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_dr, (10, 100), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, str_rd, (10, 130), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_rd, (10, 130), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(frame, str_lr, (10, 160), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_lr, (10, 160), font, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
        cv2.putText(frame, str_rl, (10, 190), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, str_rl, (10, 190), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        cv2.namedWindow("Frame", cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Frame',frame)
        
        if cv2.waitKey(66)&0xff==ord('q'):
            break

    else:
        break

cap.release()
cv2.destroyAllWindows()









