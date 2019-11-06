from math import sqrt
import os
import pickle
import numpy as np
import scipy
import scipy.spatial
# from PyQt5.QtCore import QObject

class Matcher:
    """Class untuk melakukan proses matching"""

    def __init__(self, pckPath="imgData.pck", fastAlgorithm=False):
        self.pckPath = os.path.join("pck", pckPath)
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
                    self.vectorLen.append(self.euDistHelper(vector, zeroVector))
                except Exception as e:
                    self.name.pop()
                    self.vector.pop()
        else:
            for name, vector in self.data.items():
                self.name.append(name)
                self.vector.append(vector)
                # precompute vector length
                try:
                    self.vectorLen.append(self.euDistHelper(vector, zeroVector, fastAlgorithm=True))
                except Exception as e:
                    self.name.pop()
                    self.vector.pop()
        # Create numpy array
        self.name = np.array(self.name)
        self.vector = np.array(self.vector)
        self.vectorLen = np.array(self.vectorLen)

    def euDistHelper(self, vector1, vector2, fastAlgorithm=False):
        if not(fastAlgorithm): # default algo
            sum = 0
            for i in range(len(vector1)):
                sum += (vector1[i] - vector2[i]) * (vector1[i] - vector2[i])
            return (sqrt(sum))
        else: # using numpy, for GUI testing only if needed
            return (np.linalg.norm(vector1 - vector2))

    def euDist(self, vector, fastAlgorithm=False):
        imgSimilarity = [self.euDistHelper(vector, v, fastAlgorithm=fastAlgorithm) for v in self.vector]
        imgSimilarity = np.array(imgSimilarity)
        return imgSimilarity

    def cosSimHelper(self, vector1, vector2):
        # Calculate numerator
        num = 0
        for i in range(len(vector1)):
            num += vector1[i] * vector2[i]
        return (num)

    def cosSim(self, vector, fastAlgorithm=False):
        if not(fastAlgorithm): # default algo
            imgSimilarity = []
            zeroVector = np.zeros(len(vector))
            for i in range(len(self.vector)):
                denom = self.euDistHelper(vector, zeroVector) * self.vectorLen[i]
                try:
                    assert denom != 0
                    num = self.cosSimHelper(vector, self.vector[i])
                    imgSimilarity.append(1 - num/denom)
                except AssertionError as e:
                    imgSimilarity.append(1)        # sehingga gambar yang error tidak akan dipilih jadi top imgSimilarity
                                                   # imgSimilarity, smaller value: more similar, maxVal in cosSim is 1
            imgSimilarity = np.array(imgSimilarity)
            return imgSimilarity
        else:  # using scipy, for GUI testing only if needed
            return scipy.spatial.distance.cdist(self.vector, vector.reshape(1, -1), 'cosine').reshape(-1)

    def match(self, vector, op, top=3, fastAlgorithm=False):
        try:
            if (op == "euDist"):
                imgSimilarity = self.euDist(vector, fastAlgorithm=fastAlgorithm)
            elif (op == "cosSim"):
                imgSimilarity = self.cosSim(vector, fastAlgorithm=fastAlgorithm)
            else:
                raise Exception
        except Exception as e:
            print(e)
            print("Invalid option")
        # Sort imgSimilarity, smaller value: more similar
        idxSort = np.argsort(imgSimilarity)
        nearestImgPath = self.name[idxSort][:top]
        nearestImgDist = imgSimilarity[idxSort][:top]
        return (nearestImgPath.tolist(), nearestImgDist.tolist())
