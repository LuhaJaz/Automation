from tracemalloc import Snapshot
import cv2
import dropbox
import time
import random

start_time= time.time()

def takeSnapshot():
    number= random.randint(0,100)
#Starts the webcam. 0 is the camera
    videoCaptureObject= cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result=True 
    while(result):
#Read the frames while the camera is on.
        ret,frame= videoCaptureObject.read()
#Write method is used to save an image to any storage device.
        imgName= "img"+str(number)+".png"
        cv2.imwrite(imgName, frame)
        start_time= time.time
        result= False 
    # return imgName
    print("Snapshot taken")
#Close the webcame. Release is used
    videoCaptureObject.release()
#Close any open windows by the camera
    cv2.destroyAllWindows()
takeSnapshot()