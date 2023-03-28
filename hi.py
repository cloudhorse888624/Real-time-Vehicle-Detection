# importing the module
import cv2
   
# function to display the coordinates of
# of the points clicked on the image 
def click_event(event, x, y, flags, params):
  
    # checking for left mouse clicks
    if event == cv2.EVENT_LBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, str(x) + ',' +
                    str(y), (x,y), font,
                    1, (255, 0, 0), 2)
        cv2.imshow('image', frame)
  
    # checking for right mouse clicks     
    if event==cv2.EVENT_RBUTTONDOWN:
  
        # displaying the coordinates
        # on the Shell
        print(x, ' ', y)
  
        # displaying the coordinates
        # on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        b = frame[y, x, 0]
        g = frame[y, x, 1]
        r = frame[y, x, 2]
        cv2.putText(frame, str(b) + ',' +
                    str(g) + ',' + str(r),
                    (x,y), font, 1,
                    (255, 255, 0), 2)
        cv2.imshow('image', frame)
  
# driver function
if __name__=="__main__":
    cap=cv2.VideoCapture("111.mp4")
    while(cap.isOpened()):
        ret, frame=cap.read()
        if ret==True:
  
  
            # displaying the image
            cv2.imshow('image', frame)
  
    # setting mouse handler for the image
    # and calling the click_event() function
            cv2.setMouseCallback('image', click_event)
  
    # wait for a key to be pressed to exit
            cv2.waitKey(0)
  
    # close the window
            cv2.destroyAllWindows()