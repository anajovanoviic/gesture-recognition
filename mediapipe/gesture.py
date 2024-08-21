import numpy as np
import cv2 
import matplotlib.pyplot as plt
from numpy import load

array = load('C:/Users/anadjj/programs_ana/master/gesture-recognition/mediapipe/points/array1.npy')

print(array)

x = array[0]
y = array[1]
z = array[2]

# Define the camera matrix 
fx = 800
fy = 800
cx = 640
cy = 480
camera_matrix = np.array([[fx, 0, cx], 
                          [0, fy, cy], 
                          [0, 0, 1]], np.float32) 
  
# Define the distortion coefficients 
dist_coeffs = np.zeros((5, 1), np.float32) 
points_3d = np.array([[[x, y, z]]], np.float32) 

ax = plt.axes(projection="3d")
ax.scatter(x, y, z)
plt.figure()
  
# Define the rotation and translation vectors 
rvec = np.zeros((3, 1), np.float32) 
tvec = np.zeros((3, 1), np.float32) 
  
# Map the 3D point to 2D point 
points_2d, _ = cv2.projectPoints(points_3d, 
                                 rvec, tvec, 
                                 camera_matrix, 
                                 dist_coeffs) 

# Display the 2D point 
print("2D Point:", points_2d) 
print(points_2d[0][0][0])
t = len(points_2d)
print(t)

x2 = points_2d[0][0][0]
y2 = points_2d[0][0][1]

plt.scatter(x2, y2)
#plt.figure()

plt.show()
