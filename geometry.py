import matplotlib.pyplot as plt
from colors import Color

class Coordinates:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = [x, y]

    def __repr__(self):
        return f"x: {self.x} \ny: {self.y}"
    
    def __add__(self, a, list: bool=False, dict: bool=False, set: bool=False, tuple:bool=False, coor:bool=True):
        if coor:
            ecoor = Coordinates(self.x + a.x, self.y + a.y)
            return ecoor
        if list:
            elist = [self.x + a.x, self.y + a.y]
            return elist
        if dict:
            edict = {
                'x': self.x + a.x,
                'y': self.y + a.y
            }
            return edict
        if set:
            eset = {self.x + a.x, self.y + a.y}
            return eset

        if tuple:
            etuple = (self.x + a.x, self.y + a.y)
            return etuple
        
        else:
            return "Parameters Missing"
    def __sub__(self, a, list: bool=False, dict: bool=True, set: bool=False, tuple:bool=False):
        if (list):
            elist = [self.x - a.x, self.y - a.y]
            return elist
        if (dict):
            edict = {
                'x': self.x - a.x,
                'y': self.y - a.y
            }
            return edict
        if (set):
            eset = {self.x - a.x, self.y - a.y}
            return eset

        if (tuple):
            etuple = (self.x - a.x, self.y - a.y)
            return etuple
        
        else:
            return "Parameters Missing"
        

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