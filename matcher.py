from worker import Worker

from math import sqrt
import os
import pickle
import numpy as np
import scipy
import scipy.spatial

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Matcher(QObject):
    """Class untuk melakukan proses matching"""
    # Pyqt Signals
    sgnSrcProgress = pyqtSignal(int)
    sgnSrcTotalImg = pyqtSignal(int)
    sgnSrcException = pyqtSignal(object)
    sgnSrcResult = pyqtSignal(object)
    sgnSrcDone = pyqtSignal()

    def __init__(self, pckPath="imgData.pck"):
        # QObject init
        super(Matcher, self).__init__()
        # Multithreader
        self.threadPool = QThreadPool()
        # Class property
        self.pckPath = os.path.join("pck", pckPath)

    def precalculateVector(self, fastAlgorithm=False):
        with open(self.pckPath, "rb") as f:
            self.data = pickle.load(f)
        # Parse the dictionary
        self.name = []
        self.vector = []
        self.vectorLen = []

        vectorLenSample = len(next(iter(self.data.values())))
        zeroVector = np.zeros(vectorLenSample)
        if not(fastAlgorithm):
            for name, vector in self.data.items():
                self.name.append(name)
                self.vector.append(vector)
                # precompute vector length
                try:
                    self.vectorLen.append(self.vectorDistance(vector, zeroVector))
                except Exception as e:
                    self.name.pop()
                    self.vector.pop()
        else:
            for name, vector in self.data.items():
                self.name.append(name)
                self.vector.append(vector)
                # precompute vector length
                try:
                    self.vectorLen.append(self.vectorDistance(vector, zeroVector, fastAlgorithm=True))
                except Exception as e:
                    self.name.pop()
                    self.vector.pop()
        # Create numpy array
        self.name = np.array(self.name)
        self.vector = np.array(self.vector)
        self.vectorLen = np.array(self.vectorLen)

    def vectorDistance(self, vector1, vector2, fastAlgorithm=False):
        if not(fastAlgorithm): # default algo
            sum = 0
            # calculate vector1[i] - vector2[i], i element index, and store it in vectorDiff
            vectorDiff = np.array(vector1) - np.array(vector2)
            for el in vectorDiff:
                sum += el * el
            return (sqrt(sum))
        else: # using numpy norm function, for GUI testing only if needed
            return (np.linalg.norm(vector1 - vector2))

    def euDist(self, vector, fastAlgorithm=False):
        # Init QProgressDialog
        self.sgnSrcTotalImg.emit(len(self.vector))
        counter = 0
        imgSimilarity = []
        for v in self.vector:
            imgSimilarity.append(self.vectorDistance(vector, v, fastAlgorithm=fastAlgorithm))
            # Update progress
            counter += 1
            self.sgnSrcProgress.emit(counter)
        imgSimilarity = np.array(imgSimilarity)
        return imgSimilarity

    def vectorDot(self, vector1, vector2):
        num = 0
        # calculate vector1[i] * vector2[i], i element index, and store it in vectorMult
        vectorMult = np.array(vector1) * np.array(vector2)
        for el in vectorMult:
            num += el
        return (num)

    def cosSim(self, vector, fastAlgorithm=False):
        if not(fastAlgorithm): # default algo
            # Init QProgressDialog
            self.sgnSrcTotalImg.emit(len(self.vector))
            counter = 0
            imgSimilarity = []
            zeroVector = np.zeros(len(vector))
            for i in range(len(self.vector)):
                denom = self.vectorDistance(vector, zeroVector) * self.vectorLen[i]
                try:
                    assert denom != 0
                    num = self.vectorDot(vector, self.vector[i])
                    imgSimilarity.append(1 - num/denom)
                except AssertionError as e:
                    imgSimilarity.append(1)        # sehingga gambar yang error tidak akan dipilih jadi top imgSimilarity
                                                   # imgSimilarity, smaller value: more similar, maxVal in cosSim is 1
                # Update progress
                counter += 1
                self.sgnSrcProgress.emit(counter)

            imgSimilarity = np.array(imgSimilarity)
            return imgSimilarity
        else:  # using scipy, for GUI testing only if needed
            return scipy.spatial.distance.cdist(self.vector, vector.reshape(1, -1), 'cosine').reshape(-1)

    def match(self, vector, op, top, fastAlgorithm):
        try:
            if (op == "euDist"):
                imgSimilarity = self.euDist(vector, fastAlgorithm=fastAlgorithm)
            elif (op == "cosSim"):
                imgSimilarity = self.cosSim(vector, fastAlgorithm=fastAlgorithm)
            else:
                raise Exception
        except Exception as e:
            print("Invalid option")
        # Sort imgSimilarity, smaller value: more similar
        idxSort = np.argsort(imgSimilarity)
        nearestImgPath = self.name[idxSort][:top]
        nearestImgDist = imgSimilarity[idxSort][:top]
        return (nearestImgPath.tolist(), nearestImgDist.tolist())

    # Multithreader
    def matchThreader(self, vector, op, top=3, fastAlgorithm=False):
        # Create worker instance
        worker = Worker(self.match, vector, op, top, fastAlgorithm)
        # Connect signals
        worker.signals.exception.connect(self.matchThreadException)
        worker.signals.result.connect(self.matchThreadResult)
        worker.signals.done.connect(self.matchThreadDone)
        # Run thread
        self.threadPool.start(worker)

    def matchThreadException(self, exception):
        self.sgnSrcException.emit(exception)

    def matchThreadResult(self, res):
        self.sgnSrcResult.emit(res)

    def matchThreadDone(self):
        self.sgnSrcDone.emit()
