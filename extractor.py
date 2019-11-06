import cv2 as cv
import numpy as np
from imageio import imread
import pickle
import random
import os
from PIL import Image

class Extractor:
    """Class untuk melakukan ekstraksi fitur gambar"""

    def __init__(self, pckPath="imgData.pck"):
        self.pckPath = os.path.join("pck", pckPath)
        self.algorithm = cv.KAZE_create()

    def listImageInDir(self, dirPath, checkImg=False):
        listDir = os.listdir(dirPath)
        allFiles = []
        allImages = []
        # Get all files
        for dir in listDir:
            path = os.path.join(dirPath, dir)
            if os.path.isfile(path):
                allFiles.append(path)
            else: # not a file
                allFiles += self.listImageInDir(path)
        # Cek apakah file adalah gambar jpg jika checkImg == True
        if checkImg:
            for file in allFiles:
                try:
                    img = Image.open(file)
                    if img.format == "JPEG":
                        allImages.append(file)
                except IOError:
                    continue
        else: # checkImg == False
            allImages = allFiles

        return allImages

    def extractImage(self, imgPath, size=32):
        img = imread(imgPath, pilmode="RGB")
        try:
            kps = self.algorithm.detect(img)
            kps = sorted(kps, key=lambda x: -x.response)[:size]
            kps, dsc = self.algorithm.compute(img, kps)
            dsc = dsc.flatten()
            if dsc.size < size * 64:
                dsc = np.concatenate([dsc, np.zeros(size * 64 - dsc.size)])
        except Exception as e:
            print ('Error: ', e)
            return None
        return dsc

    def extractBatch(self, batchPath, checkImg=False):
        images = self.listImageInDir(batchPath, checkImg)

        pckContent = {}
        for image in images:
            print("Image {}".format(image))
            name = image.split('/')[-1].lower()
            imgContent = self.extractImage(image)
            pckContent[name] = self.extractImage(image)

        with open(self.pckPath, "wb") as f:
            pickle.dump(pckContent, f)
