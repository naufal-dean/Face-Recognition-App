from extractor import Extractor
from matcher import Matcher

import matplotlib.pyplot as plt
from scipy.misc import imread
import os

if __name__ == '__main__':
    E = Extractor("KAZE")
    # E.extractBatch("db")
    M = Matcher()
    a = (E.extractImage(os.path.join("test", "test.jpg")))
    print(a)
