# -*- coding: utf-8 -*-

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Convolution2D, Activation, Dropout

import keras_tuner
import keras

"""
https://keras.io/guides/keras_tuner/getting_started/
"""

def create_model(height, width, depth, num_classes):
    
    ''' this architecture recalls on AlexNet a bit and on https://www.tensorflow.org/tutorials/images/cnn
    - try without padding
    - model.add(Conv2D(32, (7, 7), input_shape=(height, width, depth), padding='same', activation='relu'))
    - channel_first format for input_shape is not supported on CPU - see https://keras.io/2.15/api/layers/convolution_layers/convolution2d/#:~:text=Note%20that%20the%20channels_first%20format%20is%20currently%20not%20supported%20by%20TensorFlow%20on%20CPU.%20Defaults%20to%20%27channels_last%27.
    '''
    
    model = Sequential() #Sequential class groups a linear stack 
    model.add(Conv2D(32, (7, 7), input_shape=(depth, height, width), padding='same', activation='relu'))
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    
    # Layer 4
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    # Layer 5
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    # Layer 6
    model.add(Conv2D(64, (3, 3), padding='same', activation='relu'))
    # Layer 7
    model.add(Flatten())
    # Layer 8
    model.add(Dense(64, activation='relu'))
    # Layer 9
    model.add(Dense(num_classes, activation='softmax'))
    
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    
    return model

# https://keras.io/keras_tuner/

def build_model(hp):
    
    height = 480
    width = 640
    depth = 1  
    num_classes = 2

    model = Sequential()
    
    model.add(keras.layers.Conv2D(
        filters=hp.Int('conv1_filters_num', min_value=32, max_value=128, step=16),
        kernel_size=hp.Choice('conv1_filter_size', values = [3,7]),
        #input_shape=(depth, height, width), # channel first
        input_shape=(height, width, depth), # channel last
        padding='same',
        activation='relu'))
    
    model.add(keras.layers.MaxPooling2D(
        pool_size=(2,2),
        padding='same')) #should I put different values for pool_size to tune it or no?
    model.add(keras.layers.MaxPooling2D(
        pool_size=(2,2),
        padding='same'))
    
    # Should I decrease or increase number of filters in the next conv layer?
    # Based on the known architectures, number of filters is increased
    
    # Layer 4
    model.add(keras.layers.Conv2D(
        filters=hp.Int('conv2_filters_num', min_value=64, max_value=128, step=16),
        kernel_size=hp.Choice('conv2_filter_size', values = [3,5]),
        padding='same',
        activation='relu'))
    
    # Layer 5
    model.add(MaxPooling2D(pool_size=(2,2), padding='same'))
    
    # Layer 6
    model.add(keras.layers.Conv2D(
        filters=hp.Int('conv3_filters_num', min_value=32, max_value=128, step=16),
        kernel_size=hp.Choice('conv3_filter_size', values = [3,5]),
        padding='same',
        activation='relu'))
    
    # Layer 7
    model.add(keras.layers.Flatten())
    
    # Layer 8
    # How many units should I have in the Dense layer?
    model.add(keras.layers.Dense(
        units=hp.Int('dense1_units_num', min_value=32, max_value=128, step=16),
        activation='relu'))
    
    # Layer 9
    model.add(Dense(num_classes, activation='softmax'))
    
    learning_rate = hp.Float('lr', min_value=1e-4, max_value=1e-2, sampling='log')
    
    model.compile(
        #optimizer=keras.optimizers.Adam(learning_rate=learning_rate),
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=["accuracy"],
    )
              
    return model


def tuner(X_train, Y_train):
    
    tuner = keras_tuner.RandomSearch(
        hypermodel=build_model,
        objective='val_accuracy',
        max_trials=3,
        executions_per_trial=1, # better increase this to 2 later
        overwrite=True,
        directory="my_dir",
        project_name="gesture-recognition"
    )
    
    tuner.search_space_summary()
    
    tuner.search(X_train, Y_train, epochs=2, validation_split=0.1)
    


if __name__ == "__main__":
    
    print("model building")


    
  