import numpy as np

class AvgFilter:
    def __init__(self):
        self.prevAvg = 0
        self.k = 1

    def filter(self, x):
        alpha = (self.k - 1) / self.k
        avg = alpha * self.prevAvg + (1-alpha) * x

        self.prevAvg = avg
        self.k +=1
        return avg