import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_bond=np.array([0,0,0])
    uper_bond=np.array([255,50,255]) #with config saturation(medium elem) can adapt
    mask=cv2.inRange(hsv,lower_bond,uper_bond)#white 1 and other 0
    mask_not=cv2.bitwise_not(mask) #white 0 and other 1
    hold_white=cv2.bitwise_and(frame,frame,mask=mask)
    delete_white=cv2.bitwise_and(frame,frame,mask=mask_not)
    cv2.imshow("org",frame)
    cv2.imshow("hold_white",hold_white)
    cv2.imshow("delete_white",delete_white)
    if(cv2.waitKey(33)==ord('q')):
        break

cv2.destroyAllWindows()

cap.release()
#thanks 123