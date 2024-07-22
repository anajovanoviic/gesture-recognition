#grab images from live-stream folder

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt



# comparing image1 from main.py and frame

path = r'C:/Users/anadjj/programs_ana/master/gesture-recognition/gesture-recognition/live-stream/image0.png'

frame = Image.open(path)
print("testing")
print(frame.format)

print(frame.size)

print(frame.mode)

frame_as_array = np.array(frame)
print(frame_as_array.shape)

height, width = frame_as_array.shape[0:2]

flattened_image = frame_as_array.flatten()

image_matrix = np.array([flattened_image])
#image_matrix_2 = np.array(flattened_image) #=seventh_image

#reshaped_fimage = flattened_image.reshape(480, 640)

#plt.imshow(reshaped_fimage)

x_testreal = image_matrix.reshape(1, 1, 480, 640)

x_testreal = x_testreal.astype('float32')

x_testreal = x_testreal / 255.0


    


