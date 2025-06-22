import matplotlib.pyplot as plt
from turtle import *
from colors import Color
from number import PI
import time as tm
from math import sqrt

def pythagorean_theorem(c1, c2):
    return sqrt(c1*2 + c2*2)

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
        return self.bd + self.sd + self.h
    
class Triangle: # ONLY equilateral triangles
    def __init__(self, alture, base):
        self.h = alture
        self.b = base
    
    def __repr__(self):
        return f"Alture: {self.h}\nBase: {self.b}"
    
    def area(self):
        return self.h*self.b / 2
    
    def perimeter(self):
        return self.b*3

class Custom:
    def __init__(self, apothem, sides, sidelen):
        self.ap = apothem
        self.sides = sides
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Custom. \nApothem: {self.ap}\nSides: {self.sides}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * self.sides

    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2


class Dodecagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Dodecagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 12
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2


class Hendecagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Hendecagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 11
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2

class Decagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Decagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 10
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2

class Enneagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Enneagon. \nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 9
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2



class Octogon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Octogon. \nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 8 # Since has been already definedç
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2

class Heptagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Heptagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 7
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2


class Hexagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Hexagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"
    
    def perimeter(self):
        return self.sidelen * 6

    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2

class Pentagon:
    def __init__(self, apothem, sidelen):
        self.ap = apothem
        self.sidelen = sidelen
    
    def __repr__(self):
        return f"Pentagon.\nApothem: {self.ap}\nSide length: {self.sidelen}"

    def perimeter(self):
        return self.sidelen * 5
    
    def area(self):
        perimeter = self.perimeter()
        return self.ap * perimeter / 2

