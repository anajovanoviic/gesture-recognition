import os, cv2, re
import numpy 
import numpy as np
import sys
import process_frame
import matplotlib.pyplot as plt
import array as arr

from PIL import Image
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical
from save_model import save_model
from model import create_model
from numpy import save

sys.path.append('C:/Users/anadjj/programs_ana/master/gesture-recognition/gesture-recognition/approach-1')

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

# Literature used for the labelling part is from video from Anuj shah - https://www.youtube.com/watch?v=2pQOXjpO_u0

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

#Why do we reshape?
X_train = X_train.reshape(X_train.shape[0], 1, img_rows, img_cols)
X_test = X_test.reshape(X_test.shape[0], 1, img_rows, img_cols)


# For computation convert each of the pixel values in float to avoid overflow and underflow 
# errors typical when working with integers

#X_train = X_train.astype('float32')
#X_test = X_test.astype('float32')

# Normalization to make your system faster
# below gives values like 0.00197..., so it looks like dividing with 255 is more appropriate

#1
#normalizer = preprocessing.Normalizer()
#normalized_train_X = normalizer.fit_transform(X_train)

#2
#x_train_norm = X_train / 255.0
#x_test_norm = X_test / 255.0

X_train = X_train / 255.0
X_test = X_test / 255.0

print('X_train_shape:', X_train.shape)
print(X_train.shape[0], 'train_samples')
print(X_test.shape[0], 'test_samples')

num_classes = 2

# this needs to be done if categorical crossentropy function is used in the model.compile()
Y_train = to_categorical(y_train, num_classes)
Y_test = to_categorical(y_test, num_classes)


i = 1
random_image = X_train[i, 0]
plt.imshow(random_image, interpolation='nearest')
print("label : ", Y_train[i,:])


for i in range(0, 55, 1):
    plt.figure()  
    plt.imshow(X_test[i, 0], interpolation='nearest')
    #print("label : ", Y_train[i,:])
    


#model creation

height = 480 #rows
width = 640 #cols
depth = 1
#num_classes = 2
#num_classes = 1

model = create_model(height, width, depth, num_classes)

model.summary()


history = model.fit(X_train, Y_train, epochs=20, validation_data=(X_test, Y_test))


plt.plot(history.history['accuracy'], label='accuracy')
plt.plot(history.history['val_accuracy'], label = 'val_accuracy')

plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=2)
print(test_acc)
#print("%s: %.2f%%" % (model.metrics_names[1]), )
print(X_test)
a = arr.array('i', [1, 2, 3])
save('array.npy', a)
save('x_test.npy', X_test)
save('y_test.npy', Y_test)

#save model
save_model(model)

#Prediction on the test data
predicted_classes = model.predict(X_test)
predicted_classes = np.argmax(np.round(predicted_classes),axis=1)

i = 10
plt.imshow(X_test[i, 0], interpolation='nearest')
pred = predicted_classes[i]
plt.suptitle(f'Real label: {Y_test[i,:]}')
plt.title(f"predicted label: {pred}")
print("label : ", Y_test[i,:])
print("predicted label : ", predicted_classes[i])

for i in range(0, 5, 1):
    plt.figure()  
    plt.imshow(X_test[i, 0], interpolation='nearest')
    pred = predicted_classes[i]
    plt.suptitle(f'Real label: {Y_test[i,:]}')
    plt.title(f"predicted label: {pred}")

# https://stackoverflow.com/questions/68776790/model-predict-classes-is-deprecated-what-to-use-instead
# below code doesn't work
# print(model.predict_classes(X_test[1:5]))
# print(Y_test[1:5])

predicted_classes_real = model.predict(process_frame.x_testreal)
predicted_classes_real = np.argmax(np.round(predicted_classes_real),axis=1)
print(predicted_classes_real[0])
