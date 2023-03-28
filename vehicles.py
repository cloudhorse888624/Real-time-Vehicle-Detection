# graspcoding.com
from random import randint
import time
def capture(dots, dot1, dot2):
    x1=dots[0][0]

    y1=dots[0][1]

    x2=dots[1][0]

    y2=dots[1][1]
   
    return (dot1[1]>(y1+(y2-y1)*(dot1[0]-x1)/(x2-x1)))!=(dot2[1]>(y1+(y2-y1)*(dot2[0]-x1)/(x2-x1)))
class Car:
    tracks=[]
    def __init__(self,i,xi,yi,max_age, p1, p2, p3):
        self.i=i
        self.x=xi
        self.y=yi
        self.tracks=[]
        self.R=randint(0,255)
        self.G=randint(0,255)
        self.B=randint(0,255)
        self.done=False
        self.state='0'
        self.age=0
        self.max_age=max_age
        self.dir=[]
        self.p1=p1
        self.p2=p2
        self.p3=p3

    def getRGB(self):  #For the RGB colour
        return (self.R,self.G,self.B)
    def getTracks(self):
        return self.tracks

    def getId(self): #For the ID
        return self.i

    def getState(self):
        return self.state

    def lenDir(self):
        return len(self.dir)

    def getX(self):  #for x coordinate
        return self.x

    def getY(self):  #for y coordinate
        return self.y

    def updateCoords(self, xn, yn):
        self.age = 0
        self.tracks.append([self.x, self.y])
        self.x = xn
        self.y = yn

    def setDone(self):
        self.done = True

    def timedOut(self):
        return self.done


    def which_way(self):
        
        if len(self.tracks)>=2:
            if self.state=='1':

                if capture(self.p1, self.tracks[-1], self.tracks[-2])==True:
                    self.state='2'
                    
                    self.dir.append(1)
                    return self.dir
                elif capture(self.p2, self.tracks[-1], self.tracks[-2])==True:
                    self.state='2'
                    
                    self.dir.append(2)
                    return self.dir
                elif capture(self.p3, self.tracks[-1], self.tracks[-2])==True:
                    self.state='2'
                    
                    self.dir.append(3)
                    return self.dir
                return self.dir
            if self.state=='0': 
                if capture(self.p1, self.tracks[-1], self.tracks[-2])==True:
                    
                    self.state='1'
                    self.dir.append(1)
                    return self.dir
                elif capture(self.p2, self.tracks[-1], self.tracks[-2])==True:
                    
                    self.state='1'
                    self.dir.append(2)
                    return self.dir
                elif capture(self.p3, self.tracks[-1], self.tracks[-2])==True:
                    
                    self.state='1'
                    self.dir.append(3)
                    return self.dir
                return self.dir
        return 0
        #     if self.state=='0':
        #         if self.tracks[-1][1]<mid_end and self.tracks[-2][1]>=mid_end:
        #             state='1'
        #             self.dir='up'
        #             return True
        #         else:
        #             return False
        #     else:
        #         return False
        # else:
        #     return False

    def age_one(self):
        self.age+=1
        if self.age>self.max_age:
            self.done=True
        return  True

#Class2

class MultiCar:
    def __init__(self,cars,xi,yi):
        self.cars=cars
        self.x=xi
        self.y=yi
        self.tracks=[]
        self.R=randint(0,255)
        self.G=randint(0,255)
        self.B=randint(0,255)
        self.done=False
