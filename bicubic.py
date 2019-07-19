import cv2
import numpy as np
import math
img = cv2.imread("Lena.jpg")
h= img.shape[0]
w = img.shape[1]
new_image = np.zeros([h*2,w*2,3])

# 插值内核
def S(x):
    x = np.abs(x)
    if 0 <= x < 1:
        return 1 - 2 * x**2 + x**3
    if 1 <= x < 2:
        return 4 - 8 * x + 5 * x**2 - x**3
    else:
        return 0


def get_16_points(x,y,k):
    result = np.zeros([4,4])

    for i in range(-1,3):
        for j in range(-1,3):
            result[1+i][1+j] = img[x+i,y+j,k]
    return result


for k in range(3):
    for i in range(2,h*2-5):
        for j in range(2,w*2-5):
            x = i/2
            y = j/2

            x1 = 1 + x - int(x)
            x2 = x - int(x)
            x3 = int(x)-x + 1
            x4 = int(x)-x + 2

            y1 = 1 + y - int(y)
            y2 = y - int(y)
            y3 = int(y)-y+1
            y4 = int(y)-y+2

            A = np.matrix([[S(x1),S(x2),S(x3),S(x4)]])
            B = get_16_points(int(x),int(y),k)
            C = np.matrix([[S(y1)], [S(y2)], [S(y3)], [S(y4)]])
            new_image[i,j,k] = np.dot(np.dot(A, B),C)

cv2.imshow("new_image",np.uint8(new_image))
cv2.waitKey(0)
