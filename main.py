from extractor import Extractor
from matcher import Matcher

import matplotlib.pyplot as plt
from imageio import imread
import os

def show_img(path):
    img = imread(path, pilmode="RGB")
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    E = Extractor("miniImgData.pck")
    # E.extractBatch("miniDb")
    M = Matcher(fastAlgoritm=True)
    a = (E.extractImage(os.path.join("test", "test2.jpg")))
    # show_img(os.path.join("test", "test.jpg"))
    imgPath, imgDist = M.matcher(a, "cosSim", 20, fastAlgoritm=True)
    for i in range(20):
        print(imgPath[i])
        print(imgDist[i])
