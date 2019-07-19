import cv2
import numpy as np
import math

img = cv2.imread("Lena.jpg")
def sample_scaling(img,k1,k2):
    h = img.shape[0]
    w = img.shape[1]
    th = h//k1
    tw = w//k2
    new_img = np.zeros([th,tw,3])
    for k in range(3):
        for i in range(0, h, k1):
            for j in range(0, w, k2):
                new_img[i//k1,j//k2,k]= img[i,j,k]
    return new_img
new_img = sample_scaling(img,2,2)
cv2.imshow("new_image",np.uint8(new_img))
cv2.waitKey(0)
