import cv2
import numpy as np

img = cv2.imread('Images/messi.jpeg',1) # 0 for grayscale
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
