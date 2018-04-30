#!/usr/bin/python
import cv2
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    img = cv2.imread('wood-wristwatch-time-190819.jpg', cv2.IMREAD_GRAYSCALE)

    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #plt.imshow(img, cmap='gray', interpolation='bicubic')
    # plt.plot([50, 200], [80, 100], 'c', linewidth=5)
    #plt.show()
    cv2.imwrite('wood-wristwatch-time-190819.jpg', img)



