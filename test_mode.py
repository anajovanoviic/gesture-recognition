import cv2

capture = cv2.VideoCapture(0)

bool_value = capture.set(cv2.CAP_PROP_MODE, cv2.CAP_MODE_GRAY)

print(bool_value)
