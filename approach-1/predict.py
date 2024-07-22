#from main import model

import process_frame
import numpy as np


from keras import models

from numpy import load


def predict_gesture(image):
    
    model = models.load_model('model.h5')
    #model.summary()
    X_test = load('x_test.npy')
    Y_test = load('y_test.npy')
    test_loss, test_acc = model.evaluate(X_test, Y_test, verbose=2)
    print(test_acc)
    #print(X_test)
    
    predicted_classes_real = model.predict(process_frame.x_testreal)
    predicted_classes_real = np.argmax(np.round(predicted_classes_real),axis=1)
    
    print("predicted label:")
    print(predicted_classes_real)
    return predicted_classes_real[0]








    
