from config import *
from os import path

class Map:
    def __init__(self, filename):
        self.data = []
        with open(filename, 'rt') as f:
            for line in f:
                self.data.append(line.strip())


'''
map = Map(path.join(PROJECT_DIR, 'map.txt'))
print(map.data)
'''
