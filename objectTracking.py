# image processing 1
import cv2
import numpy as np


cv2.namedWindow("Trackbars")
cv2.moveWindow("Trackbars",320,0)
def nothing(x):
    pass

# create trackbar objects
cv2.createTrackbar("hsvLow","Trackbars",80,179,nothing)
cv2.createTrackbar("hsvHigh","Trackbars",120,179,nothing)
cv2.createTrackbar("satLow","Trackbars",104,255,nothing)
cv2.createTrackbar("satHigh","Trackbars",255,255,nothing)
cv2.createTrackbar("valLow","Trackbars",83,255,nothing)
cv2.createTrackbar("valHigh","Trackbars",255,255,nothing)


webCam=cv2.VideoCapture(0)

while True:
    ret,frame = webCam.read()

    frame = cv2.resize(frame,(640,480))
    hsvL=cv2.getTrackbarPos("hsvLow","Trackbars")
    hsvH = cv2.getTrackbarPos("hsvHigh","Trackbars")
    satL=cv2.getTrackbarPos("satLow","Trackbars")
    satH = cv2.getTrackbarPos("satHigh","Trackbars")
    valL=cv2.getTrackbarPos("valLow","Trackbars")
    valH = cv2.getTrackbarPos("valHigh","Trackbars")
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lb = np.array([hsvL,satL,valL])
    hb = np.array([hsvH,satH,valH])

    FGmask = cv2.inRange(hsv,lb,hb)
 
    # cv2.moveWindow('FGmask',400,0)
    contours,he = cv2.findContours(FGmask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours,key=lambda x:cv2.contourArea(x),reverse=True)
    for cnt in contours:
        area=cv2.contourArea(cnt)
        (x,y,w,h)=cv2.boundingRect(cnt)
        if area>=1000:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(155,117,255),2)
    # cv2.drawContours(frame,contours,-1,(255,0,0),3)   
    cv2.imshow('frame',frame)
    cv2.moveWindow('frame',0,250)
    
    if cv2.waitKey(1)==ord('q'):
        break
webCam.release()
cv2.destroyAllWindows()