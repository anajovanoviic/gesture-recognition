import os, cv2, re
import numpy 
import sys
import matplotlib.pyplot as plt
import array as arr

from PIL import Image
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from save_model import save_model
from model import create_model
from numpy import save

from model import tuner

sys.path.append('C:/Users/anadjj/programs_ana/master/gesture-recognition/gesture-recognition/approach-1')

path1 = r'C:\Users\anadjj\programs_ana\master\stari-radovi\gesture-recognition\approach-1\dataset'

path2 = r'C:\Users\anadjj\programs_ana\master\stari-radovi\gesture-recognition\approach-1\processed_dataset'

files = os.listdir(path1)
nums = sorted( int((re.search(r'\d+(\d{1,2})?', num)).group()) for num in files)
final_output = [ "image"+str(i)+".png" for i in nums]
i = 0

for file in final_output:
    i=i+1
    file_path = os.path.join(path1, file)
    img = cv2.imread(file_path, 0)
    img_resized = cv2.pyrDown(img)
    cv2.imwrite(os.path.join(path2, "image" + str(i) + '.png'), img_resized)
    
processed_images = os.listdir(path2)

#image1 = array.array('i', [Image.open(path2 + '\\' + final_output[0])])

image1 = Image.open(path2 + '\\' + final_output[0])

print(image1.format)
print(image1.size)
print(image1.mode)

array_image1 = numpy.array(image1)
print(array_image1.shape)
a, b = array_image1.shape[0:2]

#image2 = Image.open(path2 + '\\' + final_output[1])

#array_image2 = numpy.array(image2)

#num of processed images
num_processed_images = len(processed_images)

matrix = numpy.array([numpy.array(Image.open(path2 + '\\' + image)).flatten() for image in final_output],'f')

#LABELLING

label = numpy.ones((num_processed_images,),dtype = int)
label[0:141]=0
label[141:]=1

#shuffles arrays in a synchronized manner
data,Label = shuffle(matrix, label, random_state=2)
train_data = [data,Label]

seventh_img = matrix[167]
print(matrix[167].shape)

#reshaping of the flatten image(array) to the original dim in order to visualize it
img = matrix[167].reshape(480,640)
print(img.shape)


plt.imshow(img)
plt.imshow(img, cmap='gray')

print (train_data[0].shape)
print(train_data[1].shape)

'''
img2 = train_data[0]
img3 = img2[0]


test = img3.reshape(480,640)
plt.imshow(test)

print("")
print("train_data[0]")
print(train_data[0])
'''

(X, y) = (train_data[0], train_data[1])

X_train, X_test, y_train, y_test = train_test_split(train_data[0], train_data[1], test_size=0.2, random_state=4)

img_rows = 480
img_cols = 640


X_train = X_train.reshape(X_train.shape[0], img_rows, img_cols, 1) # channel_last
#X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols) # channel_first
X_train = X_train / 255.0

num_classes = 2   
Y_train = to_categorical(y_train, num_classes)

tuner(X_train, Y_train)