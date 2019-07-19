import cv2
import numpy as np
img = cv2.imread("Lena.jpg")
w= img.shape[0]
h = img.shape[1]
new_image = np.zeros([w*2,h*2,3])
for k in range(3):
    for i in range(w*2):
        for j in range(h*2):
            new_image[i,j,k] = img[i//2,j//2,k]
cv2.imshow("new_image",np.uint8(new_image))
cv2.waitKey(0)
