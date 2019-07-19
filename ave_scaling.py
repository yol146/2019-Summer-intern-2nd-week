import cv2
import numpy as np
import math

img = cv2.imread("Lena.jpg")
h= img.shape[0]
w = img.shape[1]
new_img = np.zeros([h//2,w//2,3])
height = h//2
width = h//2
for k in range(3):
    for i in range(height):
        for j in range(width):
            Px = int(i*2)
            Py = int(j*2)
            Qx = int((i+1)*2)
            Qy = int((j+1)*2)
            sum = 0
            num = (Qx-Px)*(Qy-Py)
            for x in range(Px, Qx):
                for y in range(Py, Qy):
                    sum += img[x,y,k]
            new_img[i,j,k] = sum //num
cv2.imshow("new_img",np.uint8(new_img))
cv2.waitKey(0)
