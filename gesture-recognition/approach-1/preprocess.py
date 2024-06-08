import os, cv2, re, array

import numpy 

from PIL import Image

from sklearn.utils import shuffle
import matplotlib.backend_bases
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


from sklearn import preprocessing

from model import create_model

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

path1 = r'C:\Users\anadjj\programs_ana\master\gesture-recognition\gesture-recognition\approach-1\dataset'

path2 = r'C:\Users\anadjj\programs_ana\master\gesture-recognition\gesture-recognition\approach-1\processed_dataset'

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

#num of processed images
num_processed_images = len(processed_images)

matrix = numpy.array([numpy.array(Image.open(path2 + '\\' + image)).flatten() for image in final_output],'f')

#LABELLING

label = numpy.ones((num_processed_images,),dtype = int)
label[0:141]=0
label[141:]=1

data,Label = shuffle(matrix, label, random_state=2)
train_data = [data,Label]

img = matrix[167].reshape(480,640)
plt.imshow(img)
plt.imshow(img, cmap='gray')

print (train_data[0].shape)
print(train_data[1].shape)

img2 = train_data[0]
img3 = img2[0]

test = img3.reshape(480,640)
plt.imshow(test)

print(train_data[0])

X_train, X_test, y_train, y_test = train_test_split(train_data[0], train_data[1], test_size=0.2, shuffle=False)

row = numpy.ptp(X_train,axis=1)

# Display result
print("range along the row:\n",row,"\n")



# Finding range along the column
col = numpy.ptp(X_train,axis=0)

# Display result
print("range along the column:\n",col,"\n")

for item in col:
    if item >= 255:
        print("issue")
    #else:
    #    print("no number like that")


#Normalization
#below gives values like 0.00197..., so it looks like dividing with 255 is more appropriate

#1
#normalizer = preprocessing.Normalizer()
#normalized_train_X = normalizer.fit_transform(X_train)

#2
x_train_norm = X_train / 255.0
x_test_norm = X_test / 255.0

print(x_train_norm.shape)


#model creation
height = 480
width = 640
depth = 1
num_classes = 1

model = create_model(height, width, depth, num_classes)
model.summary()

#change loss when you add more gestures, i.e. more multi-class classification
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

#history = model.fit(x_train_norm, y_train, epochs=10, validation_data=(x_test_norm, y_test))

history = model.fit(x_train_norm.reshape(-1, 480, 640, 1), y_train.reshape((-1, 1)), epochs=10, validation_data=(x_test_norm, y_test))


    