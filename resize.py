import os
import cv2 as cv
import numpy as np

path = "E:\\Programming\\OpenCV\\resize\\in"

dir_list = os.listdir(path)

maxWidth = 1200

for f in dir_list:
    img = cv.imread('in/' + f)
    width = img.shape[1]
    height = img.shape[0]
    ratio = height / width
    if width >= maxWidth or height >= maxWidth:
        if width >= height:
            new_dim = (int(maxWidth), int(ratio * maxWidth))
            dst = cv.resize(img, new_dim)
            cv.imwrite("out/" + f, dst)
            print(f + " resized to width")
        else:
            newRatio = width / height
            new_dim = (int(newRatio * maxWidth), int(maxWidth))
            dst = cv.resize(img, new_dim)
            cv.imwrite("out/" + f, dst)
            print(f + " resized to height")
    else:
        cv.imwrite("out/" + f, img)
        print(f + " is not resized")

