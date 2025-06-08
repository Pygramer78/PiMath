import geometry as gm
from random import randint, choice

class Color:
    def __init__(self, hex: str):
        self.hex = hex

def randomColor():
    return "#" +''.join([choice('0123456789ABCDEF') for j in range(6)])