import numpy as np
import argparse
import cv2
import os
import cvlib as cv
import time

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cnt=0
zz=[]
def ca(dir):
    for path,subdirnames,filenames in os.walk(dir, topdown=False):        
        for filename in filenames:         
            img_path=os.path.join(path,filename)       
            # Read the input image            
            img = cv2.imread(img_path)
            # Convert into grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect faces
            face_locations = face_cascade.detectMultiScale(gray, 1.3, 5)
            t = len(face_locations)
            print(len(face_locations))
            if(len(face_locations)==1):
                pass
            else:
                global cnt
                cnt=cnt+1
                zz.append(img_path)
                       

ca('images')
print("count=",cnt)
print(zz)
