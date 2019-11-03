from math import sqrt
import os
import pickle
import numpy as np

class Matcher:
    """Class untuk melakukan proses matching"""

    def __init__(self, pckPath="imgData.pck"):
        self.pckPath = os.path.join("pck", pckPath)
        with open(self.pckPath, "rb") as f:
            self.data = pickle.load(f)
        # Parse the dictionary
        self.name = []
        self.vector = []
        for name, vector in self.data.items():
            self.name.append(name)
            self.vector.append(vector)
        self.name = np.array(self.name)
        self.vector = np.array(self.vector)

    def euDistHelper(self, vector1, vector2):
        sum = 0
        for i in range(len(vector1)):
            sum += (vector1[i] - vector2[i]) ** 2
        return (sqrt(sum))

    def euDist(self, vector):
        imgSimilarity = [self.euDistHelper(vector, self.vector[i]) for i in range(len(self.vector))]
        return imgSimilarity

    def cosSimHelper(self, vector1, vector2):
        denom = self.euDistHelper(vector1, np.zeros(len(vector1))) * \
                self.euDistHelper(vector2, np.zeros(len(vector2)))
        try:
            assert denom != 0
        except AssertionError as e:
            print("Error: ", e)
            return None
        # Calculate numerator
        num = 0
        for i in range(len(vector1)):
            num += vector1[i] * vector2[i]
        return (num / denom)

    def cosSim(self, vector):
        imgSimilarity = [(1 - self.cosSimHelper(vector, self.vector[i])) for i in range(len(self.vector))]
        return imgSimilarity

    def matcher(self, vector, op, top=3):
        try:
            if (op == "euDist"):
                imgSimilarity = self.euDist(vector)
            elif (op == "cosSim"):
                imgSimilarity = self.cosSim(vector)
            else:
                raise Exception
        except Exception as e:
            print(e)
            print("Invalid option")
        # Sort imgSimilarity, smaller value: more similar
        idxSort = np.argsort(imgSimilarity)
        nearestImgPath = self.name[idxSort][:3]
        nearestImgDist = imgSimilarity[idxSort][:3]
        return (nearestImgPath.tolist(), nearestImgDist.tolist())
