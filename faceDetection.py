import cv2
import numpy as np
from threading import *
import time




face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

Video = cv2.VideoCapture(0)
time.sleep(3)



def face(faces):
    dimension=len(faces)
    if (dimension!=0):
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    else:
        pass

            
while True:
    check,frame=Video.read()

    faces=face_cascade.detectMultiScale(frame)
    face(faces)
    cv2.imshow('Captures',frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
Video.release() 
cv2.destroyAllWindows()
