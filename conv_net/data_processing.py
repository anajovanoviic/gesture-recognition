import os
import re, cv2

dir_path = os.path.dirname(os.path.realpath(__file__))
substring1 = r'G1'
i=0 
path = "C:\\Users\\anadjj\\programs_ana\\master\\gesture-recognition\\gesture-recognition\\approach-1\\dataset"

for root, dirs, files in os.walk(dir_path):
    for file in files: 
        if re.search(substring1, root) and "G10" not in root:
            if file.endswith('rgb.png'): 
                i=i+1
                print (root+'/'+str(file))
                img = cv2.imread(root+'/'+str(file))
                os.chdir(path)
                cv2.imwrite('image' + str(i) + '.png', img)

substring2 = r'G2'

for root, dirs, files in os.walk(dir_path):
    for file in files: 
        if re.search(substring2, root):
            if file.endswith('rgb.png'): 
                i=i+1
                print (root+'/'+str(file))
                img = cv2.imread(root+'/'+str(file))
                os.chdir(path)
                cv2.imwrite('image' + str(i) + '.png', img)

         
