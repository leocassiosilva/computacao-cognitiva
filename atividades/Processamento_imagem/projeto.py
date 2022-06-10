import cv2
from skimage.filters import roberts, sobel, scharr, prewitt
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread(
    '/home/leocassio/PycharmProjects/computacao-cognitiva/atividades/Processamento_imagem/imgs/folhas/001.jpg')
green_image = img.copy()
green_image[:, :, 0] = 0
green_image[:, :, 2] = 0
#img_g = img[:, :, 1]


cv2.imshow('G-RGB', green_image)
cv2.waitKey(0)
cv2.namedWindow("G-RGB", cv2.WINDOW_AUTOSIZE)

print(green_image)
# Segmentação
