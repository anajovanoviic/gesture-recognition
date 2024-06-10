# -*- coding: utf-8 -*-

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Convolution2D, Activation, Dropout


def create_model(height, width, depth, num_classes):
    
    #this architecture recalls on AlexNet a bit and on https://www.tensorflow.org/tutorials/images/cnn
    model = Sequential() #Sequential class groups a linear stack 
    #try without padding
    #model.add(Conv2D(32, (7, 7), input_shape=(height, width, depth), padding='same', activation='relu'))
    model.add(Conv2D(32, (7, 7), input_shape=(depth, height, width), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    model.add(Flatten())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    return model


    
  