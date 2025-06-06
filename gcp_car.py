import numpy as np
import cv2
import keyboard
import pydirectinput
import time

cap = cv2.VideoCapture(0)
#keyboard = Controller()

while 1:
    b,frame=cap.read()
    img = cv2.resize(frame,(640,360))
    img=cv2.flip(img,1)
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    cv2.rectangle(img,(0,0),(315,165),(255,0,0),2)
    cv2.putText(img,'LEFT',(0,50),cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    
    cv2.rectangle(img,(320,0),(640,165),(255,0,0),2)
    cv2.putText(img,'RIGHT', (460,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255))
    
    cv2.rectangle(img,(220,170),(420,270),(255,0,0),2)
    cv2.putText(img,'ACCELERATE',(227,220),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
   
    cv2.rectangle(img,(0,275),(640,360),(255,0,0),2)
    cv2.putText(img,'BRAKE',(270,315),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255))
    
    l_col=np.array([20,100,100])
    u_col=np.array([30,255,255])
     
    mask=cv2.inRange(hsv,l_col, u_col)
    kernel=np.ones((5,5),np.uint8)
    mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask=cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    bluecnts,hierarchy = cv2.findContours(mask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    
    if len(bluecnts)>0:
        l=[]
        for conts in bluecnts:
            area=cv2.contourArea(conts)
            if area>300:
                x,y,w,h=cv2.boundingRect(conts)
                cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),2)
                cv2.circle(img,(int(x+x+w)/2),int((y+y+h)/2),2,(255,255,255),2)
                l.append((x,y,w,h))
                
            #print('List is',L)
             #print('Length of L', Len(L))
             
        try:
            one=l[0]
            two=l[1]
            cen_one_x=int((one[0]+one[0]+one[2])/2)
            cen_one_y=int((one[1]+one[1]+one[3])/2)
            
            cen_two_x=int((two[0]+two[0]+two[2])/2)
            cen_two_y=int((two[1]+two[1]+two[3])/2)
            
            cv2.line(img,(cen_one_x,cen_one_y),(cen_two_x,cen_two_y),(0,255,0),2)
        except:
            pass
       
        try:
            x1,y1=cen_one_x,cen_one_y
            x2,y2=cen_two_x,cen_two_y
            #print('center one', x1,y1)
            if (220 < x1 < 420) and (165 < y1 < 270) and (220 < x2 < 420) and (165 < y2 <270):
                print('UP')
                pydirectinput.keyDown('up')
                #time.sleep(0.01)
                pydirectinput.keyUp('up')
                #keyboard.release(key.up)
            if (0 < x1 < 640) and (271 < y1 < 360) and (0 < x2 < 640) and (271 < y2 < 360):
                print('DOWN')
                pydirectinput.keyDown('down')
                #time.sleep(0.01)
                pydirectinput.keyUp('down')
                #keyboard.release(key.down)
                
            if (320 < x2 < 640) and (0 < y2 < 165):
               print('RIGHT')
               pydirectinput.keyDown('right')
               pydirectinput.keyDown('up')
               #time.sleep(0.01)
               pydirectinput.keyUp('right')
               pydirectinput.keyUp('up')
               #keyborad.release(key.right)

            if ((0 < x1 < 315) and (0 < y1 < 165)) or ((0 < x2 < 315) and (0 < y2 < 165)):
               print('LEFT')
               pydirectinput.keyDown('left')
               pydirectinput.keyDown('left')
               #time.sleep(0.01)
               pydirectinput.keyUp('left')
               pydirectinput.keyUp('left')
               #keyboard.releas(key.left)
               
            if (0 < x1 < 220) and (165 < y1 < 270) and (420 < x2 < 640) and (420 < y2 < 270):
              pydirectinput.Keyup('up')
              pydirectinput.keyUp('down')
              
        except:
          pass
       
      ##cv2.imshow('mask',mask)
    cv2.imshow('img',img)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
        
       
            