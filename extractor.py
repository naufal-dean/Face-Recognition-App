from worker import Worker

import cv2 as cv
import numpy as np
from imageio import imread
import pickle
import random
import os
from PIL import Image

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Extractor(QObject):
    """Class untuk melakukan ekstraksi fitur gambar"""
    # Pyqt Signals
    sgnExtProgress = pyqtSignal(int)
    sgnExtTotalImg = pyqtSignal(int)
    sgnExtException = pyqtSignal(object)
    sgnExtDone = pyqtSignal()

    def __init__(self, pckPath="imgData.pck"):
        # QObject init
        super(Extractor, self).__init__()
        # Multithreader
        self.threadPool = QThreadPool()
        # Class property
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

    def extractBatch(self, batchPath, checkImg):
        images = self.listImageInDir(batchPath, checkImg)

        # Init QProgressDialog
        self.sgnExtTotalImg.emit(len(images))
        counter = 0
        pckContent = {}
        for image in images:
            name = image.split('/')[-1].lower()
            imgContent = self.extractImage(image)
            pckContent[name] = self.extractImage(image)
            # Update progress
            counter += 1
            self.sgnExtProgress.emit(counter)
            print("Image {}".format(image))

        with open(self.pckPath, "wb") as f:
            pickle.dump(pckContent, f)

    # Multithreader
    def extractBatchThreader(self, batchPath, checkImg=False):
        # Create worker instance
        worker = Worker(self.extractBatch, batchPath, checkImg)
        # Connect signals
        worker.signals.exception.connect(self.extractBatchThreadException)
        worker.signals.done.connect(self.extractBatchThreadDone)
        # Run thread
        self.threadPool.start(worker)

    def extractBatchThreadException(self, exception):
        self.sgnExtException.emit(exception)

    def extractBatchThreadDone(self):
        self.sgnExtDone.emit()
