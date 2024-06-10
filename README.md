# gesture-recognition
Dataset used: Microsoft Kinect and Leap Motion Dataset, https://lttm.dei.unipd.it/downloads/gesture/#kinect_leap <br>

Approach 1, results, branch *first-step-fix*:

```
In [92]: history = model.fit(X_train, Y_train, epochs=20, validation_data=(X_test, Y_test))
Epoch 1/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 7s 1s/step - accuracy: 0.5672 - loss: 0.6807 - val_accuracy: 0.5179 - val_loss: 0.6897
Epoch 2/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 8s 965ms/step - accuracy: 0.5662 - loss: 0.6824 - val_accuracy: 0.5536 - val_loss: 0.6850
Epoch 3/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 884ms/step - accuracy: 0.5392 - loss: 0.6707 - val_accuracy: 0.5357 - val_loss: 0.6815
Epoch 4/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 860ms/step - accuracy: 0.5624 - loss: 0.6547 - val_accuracy: 0.5714 - val_loss: 0.7195
Epoch 5/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 791ms/step - accuracy: 0.5682 - loss: 0.6613 - val_accuracy: 0.5893 - val_loss: 0.6991
Epoch 6/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 817ms/step - accuracy: 0.6506 - loss: 0.6302 - val_accuracy: 0.5893 - val_loss: 0.6664
Epoch 7/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 837ms/step - accuracy: 0.6363 - loss: 0.6357 - val_accuracy: 0.4643 - val_loss: 0.7343
Epoch 8/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 786ms/step - accuracy: 0.5436 - loss: 0.6851 - val_accuracy: 0.5893 - val_loss: 0.6711
Epoch 9/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 820ms/step - accuracy: 0.6360 - loss: 0.6464 - val_accuracy: 0.5179 - val_loss: 0.7142
Epoch 10/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 795ms/step - accuracy: 0.6682 - loss: 0.6464 - val_accuracy: 0.5179 - val_loss: 0.6842
Epoch 11/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 797ms/step - accuracy: 0.6497 - loss: 0.6174 - val_accuracy: 0.5536 - val_loss: 0.6214
Epoch 12/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 785ms/step - accuracy: 0.7285 - loss: 0.5780 - val_accuracy: 0.5714 - val_loss: 0.6544
Epoch 13/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 780ms/step - accuracy: 0.7088 - loss: 0.5466 - val_accuracy: 0.6786 - val_loss: 0.5623
Epoch 14/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 784ms/step - accuracy: 0.7165 - loss: 0.5446 - val_accuracy: 0.7143 - val_loss: 0.5335
Epoch 15/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 776ms/step - accuracy: 0.7828 - loss: 0.4933 - val_accuracy: 0.6607 - val_loss: 0.5391
Epoch 16/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 778ms/step - accuracy: 0.7523 - loss: 0.5059 - val_accuracy: 0.7679 - val_loss: 0.4412
Epoch 17/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 842ms/step - accuracy: 0.7887 - loss: 0.4322 - val_accuracy: 0.7143 - val_loss: 0.5396
Epoch 18/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 800ms/step - accuracy: 0.8093 - loss: 0.3934 - val_accuracy: 0.8214 - val_loss: 0.3887
Epoch 19/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 776ms/step - accuracy: 0.8135 - loss: 0.3816 - val_accuracy: 0.8214 - val_loss: 0.4255
Epoch 20/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 801ms/step - accuracy: 0.8125 - loss: 0.3762 - val_accuracy: 0.8571 - val_loss: 0.3385
```

Graph:

![Figure 2024-06-10 first-step-fix](https://github.com/anajovanoviic/gesture-recognition/assets/51513732/5dab3a27-9f22-4f26-beca-0452900e0dd9)
