from extractor import Extractor
from matcher import Matcher

import matplotlib.pyplot as plt
from imageio import imread
import os

import timeit

def show_img(path):
    img = imread(path, pilmode="RGB")
    plt.imshow(img)
    plt.show()

if __name__ == '__main__':
    E = Extractor("KAZE", "miniImgData.pck")
    # E.extractBatch("miniDb")
    M = Matcher()
    a = (E.extractImage(os.path.join("test", "test.jpg")))
    show_img(os.path.join("test", "test.jpg"))
    imgPath, imgDist = M.matcher(a, "euDist")
    print(imgPath[0])
    print(imgDist[0])
    # for i in imgPath:
    #     print (i)
