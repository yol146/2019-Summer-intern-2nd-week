import cv2
import numpy as np
import math
img = cv2.imread("Lena.jpg")
h= img.shape[0]
w = img.shape[1]
new_image = np.zeros([h*2,w*2,3])
for k in range(3):
    for i in range(h*2-2):
        for j in range(w*2-2):
            x = i/2
            y = j/2
            p1 = img[int(x),int(y),k]
            p2 = img[int(x),int(y)+1,k]
            p3 = img[int(x)+1,int(y),k]
            p4 = img[int(x)+1,int(y)+1,k]
            Q1 = (int(y)+1-y)*p1 + (y-int(y))*p2
            Q2 = (int(y)+1-y)*p3 + (y-int(y))*p4
            new_image[i, j, k] = (int(x)+1-x)*Q1 + (x-int(x))*Q2

cv2.imshow("new_image",np.uint8(new_image))
cv2.waitKey(0)
