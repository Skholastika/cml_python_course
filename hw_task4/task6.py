import numpy as np
import re


class DataAnalyzer:

    def __init__(self, path: str):
        self.data = None
        self.path = path

    def read(self):
        self.data = np.genfromtxt(self.path, delimiter=',', dtype=str)

    def find(self, rstring: str):
        matches = np.full(self.data.shape, None)
        for n in range(self.data.shape[0]):
            for m in range(self.data.shape[1]):
                matches[n][m] = re.findall(rstring, self.data[n][m])
        return matches


D = DataAnalyzer('data.txt')
D.read()
print(D.find(r'ma'))
print(D.find(r'ma')[0][0])
