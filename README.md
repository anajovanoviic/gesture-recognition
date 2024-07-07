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


## Update July 7, 2024


Након што сам покренула тренирање добила сам другачије и лошије резултате иако у коду нисам ништа мењала. Код са којим сам добила лошије резултате -  
```
Epoch 1/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 8s 789ms/step - accuracy: 0.4134 - loss: 0.8141 - val_accuracy: 0.5179 - val_loss: 0.7053
Epoch 2/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 699ms/step - accuracy: 0.5213 - loss: 0.7000 - val_accuracy: 0.4821 - val_loss: 0.7003
Epoch 3/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 697ms/step - accuracy: 0.5154 - loss: 0.6922 - val_accuracy: 0.5179 - val_loss: 0.6907
Epoch 4/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 701ms/step - accuracy: 0.5043 - loss: 0.6948 - val_accuracy: 0.4821 - val_loss: 0.6933
Epoch 5/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 681ms/step - accuracy: 0.5049 - loss: 0.6922 - val_accuracy: 0.4821 - val_loss: 0.6980
Epoch 6/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 680ms/step - accuracy: 0.4945 - loss: 0.6954 - val_accuracy: 0.6071 - val_loss: 0.6897
Epoch 7/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 683ms/step - accuracy: 0.5768 - loss: 0.6910 - val_accuracy: 0.6071 - val_loss: 0.6891
Epoch 8/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 682ms/step - accuracy: 0.5513 - loss: 0.6900 - val_accuracy: 0.5536 - val_loss: 0.6897
Epoch 9/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 678ms/step - accuracy: 0.5387 - loss: 0.6881 - val_accuracy: 0.5536 - val_loss: 0.6888
Epoch 10/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 674ms/step - accuracy: 0.5644 - loss: 0.6847 - val_accuracy: 0.6250 - val_loss: 0.6835
Epoch 11/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 681ms/step - accuracy: 0.5812 - loss: 0.6845 - val_accuracy: 0.6071 - val_loss: 0.6821
Epoch 12/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 684ms/step - accuracy: 0.6137 - loss: 0.6748 - val_accuracy: 0.5893 - val_loss: 0.6708
Epoch 13/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 679ms/step - accuracy: 0.6526 - loss: 0.6653 - val_accuracy: 0.5536 - val_loss: 0.6581
Epoch 14/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 693ms/step - accuracy: 0.6661 - loss: 0.6584 - val_accuracy: 0.5179 - val_loss: 0.6976
Epoch 15/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 681ms/step - accuracy: 0.5801 - loss: 0.6715 - val_accuracy: 0.5179 - val_loss: 0.7169
Epoch 16/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 690ms/step - accuracy: 0.5555 - loss: 0.6942 - val_accuracy: 0.4821 - val_loss: 0.7493
Epoch 17/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 725ms/step - accuracy: 0.5013 - loss: 0.7234 - val_accuracy: 0.6071 - val_loss: 0.6812
Epoch 18/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 5s 720ms/step - accuracy: 0.6212 - loss: 0.6768 - val_accuracy: 0.5000 - val_loss: 0.7441
Epoch 19/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 803ms/step - accuracy: 0.5328 - loss: 0.7111 - val_accuracy: 0.6071 - val_loss: 0.6690
Epoch 20/20
7/7 ━━━━━━━━━━━━━━━━━━━━ 6s 780ms/step - accuracy: 0.6226 - loss: 0.6605 - val_accuracy: 0.5357 - val_loss: 0.6648
2/2 - 0s - 63ms/step - accuracy: 0.5357 - loss: 0.6648
0.5357142686843872
```

![alt text](<Figure 2024-07-07 140206 real-time-images.png>)
