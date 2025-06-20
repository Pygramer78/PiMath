import matplotlib.pyplot as plt
from turtle import *
from colors import Color
from number import PI
import time as tm
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

class Rectangles:
    def __init__(self, alture, base):
        self.h = alture
        self.b = base

    def __repr__(self):
        return f"Alture (h): {self.h} \nBase (b): {self.b}"
    
    def area(self):
        return self.h * self.b
    
    def perimeter(self):
        return self.h*2 + self.b*2


class Square:
    def __init__(self, sidelen):
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Side lenght: {self.sidelen}"

    def area(self):
        return self.sidelen**2

    def perimeter(self):
        return self.sidelen*4

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.diameter = radius * 2
    
    def __repr__(self):
        return f"Radius: {self.radius}\nDiameter: {self.diameter}"
    
    def area(self):
        return self.radius**2 / PI

class Trapeze:
    def __init__(self, BigD, Smalld, Alture):
        self.bd = BigD
        self.sd = Smalld
        self.h = Alture
    
    def __repr__(self):
        return f"Alture: {self.h}\nBig Diagonal: {self.bd}\nSmall Diagonal: {self.sd}"
    
    def area(self):
        return (self.bd + self.sd)*self.h / 2
    
    def perimeter(self):
        return "In development."
    
class Triangle:
    def __init__(self, alture, base):
        self.h = alture
        self.b = base
    
    def __repr__(self):
        return f"Alture: {self.h}\nBase: {self.b}"
    
    def area(self):
        return self.h*self.b / 2
    
    def perimeter(self):
        return "Development."