from time import time
import cv2

#https://docs.opencv.org/4.9.0/dd/d43/tutorial_py_video_display.html

cam = cv2.VideoCapture(0)

previous = time()
delta = 0
i=0

while True:
    
    current = time()
    delta += current - previous
    previous = current
    
    if delta > 3 and i <= 6:
        retval, image = cam.read()
        img = cv2.imwrite(r"C:\Users\anadjj\programs_ana\master\gesture-recognition\gesture-recognition\live-stream\image"+str(i)+".png", image)
        i += 1
        delta = 0  
        
    _, img = cam.read()
    cv2.imshow("Frame", img)
    if cv2.waitKey(1) == ord('q'):
        break