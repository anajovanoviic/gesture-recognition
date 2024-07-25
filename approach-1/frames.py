from time import time, sleep
import cv2
from predict import predict_gesture

#https://docs.opencv.org/4.9.0/dd/d43/tutorial_py_video_display.html

# function capture_frames could be made here
# no issues when running this file in spyder, but errors encoountered in vscode

cam = cv2.VideoCapture(0)

previous = time()
delta = 0
i=0
prediction = 5

while True:
    
    current = time()
    delta += current - previous
    previous = current
    
    if delta > 3 and i <= 6:
        # OpenCV uses BGR color space
        retval, image = cam.read() 
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        img = cv2.imwrite(r"C:\Users\anadjj\programs_ana\master\stari-radovi\gesture-recognition\live-stream"+str(i)+".png", image)
        prediction = predict_gesture(img)
        #prediction = i+1 #testing
        i += 1
        delta = 0  
        
       
    _, img = cam.read()
    img = cv2.putText(img, f'{prediction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    cv2.imshow("Frame", img)
    if cv2.waitKey(1) == ord('q'):
        break