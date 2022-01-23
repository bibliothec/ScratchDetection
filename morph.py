import cv2
import numpy as np
import sys
import os

args=sys.argv
img_file=args[1]
img=cv2.imread(img_file,0)
kernel=np.ones((5,5),np.uint8)
opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
sub=img-opening
img=os.path.splitext(img_file)[0]
output="./"+img+"output.png"
cv2.imwrite(output,sub)
