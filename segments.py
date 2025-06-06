import matplotlib.pyplot as plt
import coordinates as cp
from colors import Color

class Segments:
    def __init__(self, x: list):
        self.x = x
    
    def draw(self, color: Color="#000000"):
        for x, y in self.x:
            plt.scatter(x, y, c=color.hex)
        plt.show()

"""
def SegToCoor(a: Segments):
    s = 0
    s2 = 0
    result = cp.Coordinates(s, s2)
    for x, y in a.x:
        s = x
        s2 = y
    return result
# Still in development
"""