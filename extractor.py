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
    sgnExtProgress = pyqtSignal()
    sgnExtTotalImg = pyqtSignal(int)
    sgnExtException = pyqtSignal(object)
    sgnExtStatus = pyqtSignal(int, int)
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

    def extractBatch(self, batchPath, checkImg, images):
        self.pckContent = {}
        for image in images:
            name = image.split('/')[-1].lower()
            imgContent = self.extractImage(image)
            self.pckContent[name] = imgContent
            # Update progress
            self.sgnExtProgress.emit()
            print("Image {}".format(image))

    # Multithreader
    def extractBatchThreader(self, batchPath, thread=1, checkImg=False):
        # List images in db
        images = self.listImageInDir(batchPath, checkImg)
        # Init QProgressDialog
        self.sgnExtTotalImg.emit(len(images))
        # Save thread used and thread done
        self.threadUsed = thread
        self.threadDone = 0

        # Create worker instance
        workers = []
        stopIdx = 0 # initialize stopIdx, used if thread = 1
        for i in range(thread - 1):
            startIdx = i * (len(images) // thread)
            stopIdx = (i + 1) * (len(images) // thread)
            workers.append(Worker(self.extractBatch, batchPath, checkImg, images[startIdx:stopIdx]))
        workers.append(Worker(self.extractBatch, batchPath, checkImg, images[stopIdx:]))

        # Connect and run
        for worker in workers:
            # Connect signals
            worker.signals.exception.connect(self.extractBatchThreadException)
            worker.signals.done.connect(self.extractBatchThreadDone)
            # Run thread
            self.threadPool.start(worker)

    def extractBatchThreadException(self, exception):
        self.sgnExtException.emit(exception)

    def extractBatchThreadStatus(self, activeThread, maxThread):
        self.sgnExtStatus.emit(activeThread, maxThread)

    def extractBatchThreadDone(self):
        self.threadDone += 1
        self.extractBatchThreadStatus(self.threadPool.activeThreadCount(), self.threadPool.maxThreadCount())
        if self.threadDone == self.threadUsed:
            with open(self.pckPath, "wb") as f:
                pickle.dump(self.pckContent, f)
            # Reset variable
            self.threadDone = 0
            self.threadUsed = 0
            # Send all done signal to mainWindowUI
            self.sgnExtDone.emit()
