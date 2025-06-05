from number import *
from coordinates import *
from primes import *
from roman import *
from segments import *

# Known numbers:
print(f"pi number: {PI}")
print(f"euler number: {EULER}")
print(f"golden ratio number: {GOLDEN_RATIO}")
print(f"kaprekar number: {KAPREKAR}")

# Coordinates
coordenate = Coordinates(10, -10)
p = Coordinates(-10, 10)
coordenate - p # Returns another coordinate with the subtraction
