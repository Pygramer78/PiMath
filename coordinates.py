import colors as cl

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