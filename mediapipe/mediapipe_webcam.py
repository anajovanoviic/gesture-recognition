import cv2
import mediapipe as mp
import os
import posixpath
from numpy import save

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        # press 's' to save coordinate; ascii code 
        if cv2.waitKey(5) & 0xFF == 115:
          lm_0 = hand_landmarks.landmark[0] #first point
          print('hand_landmarks x:', lm_0.x)
          print('hand_landmarks:', hand_landmarks)
          print(type(lm_0))
          #save image and pass the image to the 
          #write to csv
          
          #for landmark in hand_landmarks:
          #  print(landmark[0])
          hand_dict = {}
          for i in range(21):
            array1 = []
            dict = {}
  
            
            point = hand_landmarks.landmark[i]
            print(hand_landmarks.landmark[i])
            print(point.x)
            
            #dict['key'] = [point.x, point.y, point.z]
            #dict['key'].append(point.x)
            #dict.setdefault(i, []) == [point.x, point.y, point.z]
            dict.setdefault(i, []).append(point.x)
            dict.setdefault(i, []).append(point.y)
            dict.setdefault(i, []).append(point.z)
            
            
           # dict[i].append(point.y)
            #dict[i].append(point.z)
            
            print(dict)
            #save('points/array1.npy', array1)
            #path = os.path.join('points', 'array1.npy')
            #modified_path = path.replace("\\","/")
            #save(os.path.join('points', 'array1.npy'), array1)
            
            joined_path = posixpath.join("C:/Users/anadjj/programs_ana/master_thesis_final/gesture-recognition/mediapipe/points", f"array{i+1}.npy")
            save(joined_path, dict[i])
            
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break

cap.release()