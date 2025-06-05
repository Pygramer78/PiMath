import matplotlib.pyplot as plt
import coordinates as cp
from colors import Color

class Segments:
    def __init__(self, xy: cp.Coordinates):
        self.coor = xy.coordinates
        self.x = self.coor[0]
        self.y = self.coor[1]
    
    def draw(self, color: Color):
        plt.scatter(self.x, self.y, c=color)

