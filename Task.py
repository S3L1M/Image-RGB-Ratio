import numpy as np
import PIL.Image as img
import scipy.misc as px
import math
import os

im = img.open("images.jpeg")
max = im.width
im.show()

pixels = im.load()
size = range(0, max)
data = np.empty((max, max, 3), int)
matR = np.empty((max, max), int)
matG = np.empty((max, max), int)
matB = np.empty((max, max), int)

for i in size:
    for j in size:
        matR[i, j] = pixels[j, i][0]
        matG[i, j] = pixels[j, i][1]
        matB[i, j] = pixels[j, i][2]

CMax = float(max*max*255)
ratioR = " " + str(np.sum(matR)/CMax)
ratioG = " " + str(np.sum(matG)/CMax)
ratioB = " " + str(np.sum(matB)/CMax)
invR = np.linalg.inv(matR)
ratioRv = " " + str(np.sum(invR)/CMax)

for i in size:
    for j in size:
        data[i, j, 0] = math.floor(invR[i, j] + 0.5)
        data[i, j, 1] = pixels[j, i][1]
        data[i, j, 2] = pixels[j, i][2]

# print(data)
im1 = px.toimage(data)
im1.show()

os.system("python extract_scene.py -p example_scenes.py showRatio"+ratioR+ratioG+ratioB+ratioRv)
