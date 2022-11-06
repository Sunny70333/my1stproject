import cv2
import numpy as np

def nothing(x):
    pass
def createTrackbar():
    cv2.namedWindow("thresholding")
    cv2.createTrackbar("Hue min","thresholding",0,179,nothing)
    cv2.createTrackbar("Hue max","thresholding",179,179,nothing)
    cv2.createTrackbar("sat min","thresholding",0,255,nothing)
    cv2.createTrackbar("sat max","thresholding",255,255,nothing)
    cv2.createTrackbar("val min","thresholding",0,255,nothing)
    cv2.createTrackbar("val max","thresholding",255,255,nothing)


img =cv2.imread('Images/hand.jpg')
cv2.imshow("original image",img)
gray_scale =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("gray sacle image",gray_scale)

createTrackbar()

while True:
    #T=cv2.getTrackbarPos("T","thresholding")
    #print(T)
    #img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    #lower=np.array([0,0,0])q
    #upper=np.array([180,255,255])
    #thresh_img=cv2.inRange(img,lower,upper)gra

    #_,thresh_img=cv2.threshold(gray_scale,T,255,cv2.THRESH_BINARY)
    #cv2.imshow("thresh image",thresh_img)
    img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    huemin=cv2.getTrackbarPos("Hue min","thresholding")
    huemax=cv2.getTrackbarPos("Hue max","thresholding")
    satmin=cv2.getTrackbarPos("sat min","thresholding")
    satmax=cv2.getTrackbarPos("sat max","thresholding")
    valmin=cv2.getTrackbarPos("val min","thresholding")
    valmax=cv2.getTrackbarPos("val max","thresholding")
    lower=np.array([huemin,satmin,valmin])
    upper=np.array([huemax,satmax,valmax])
    print(lower,upper)
    thresh_img=cv2.inRange(img_hsv,lower,upper)
    cv2.imshow("thresh image",thresh_img)
    imgCopy=img.copy()
    contours,_=cv2.findContours(thresh_img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(imgCopy,contours,-1,(0,0,255),2)

    cv2.imshow("original image",imgCopy)

    key=cv2.waitKey(1)
    if(key==ord('q')):
        break
cv2.destroyAllWindows()
cv2.waitKey(0)