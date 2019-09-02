import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

font = cv2.FONT_HERSHEY_SIMPLEX

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        #   getting color information
        blue = img[y, x, 0]     # (x, y, BGR)
        green = img[y, x, 1]
        red = img[y, x, 2]

        # create a window with color
        myColorImage = np.zeros((512,512,3), np.uint8)
        myColorImage[:] = [blue,green,red]
        # Convert BGR to HSV
        HSVColor = np.uint8([[[blue, green, red]]])
        myHSV = cv2.cvtColor(HSVColor, cv2.COLOR_BGR2HSV)
        # draw colors on window 
        strBGR = 'BGR: ' + str(blue) + ', ' + str(green) + ', ' + str(red)
        strHSV = 'HSV: ' + str(myHSV[0][0][0]) + ', ' + str(myHSV[0][0][1]) + ', ' + str(myHSV[0][0][2])
        cv2.putText(myColorImage, strBGR, (10,30), font, 1, (0,255,0), 2)
        cv2.putText(myColorImage, strHSV, (10,100), font, 1, (0,255,0), 2)

        cv2.imshow('image', img)
        cv2.imshow('color', myColorImage)

def scaleImage(img):
        W = 500
        height, width, depth = img.shape
        imgScale = W/width
        newX,newY = img.shape[1]*imgScale, img.shape[0]*imgScale
        newimg = cv2.resize(img,(int(newX),int(newY)))

        return newimg



#the root window
Tk().withdraw()
# show an "Open" dialog box and return the path to the selected file
filename = askopenfilename() 
      
img = cv2.imread(filename)
img = scaleImage(img)

cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()