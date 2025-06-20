from PiMath.number import *
from PiMath.geometry import *
from PiMath.primes import *
from PiMath.roman import *
from PiMath.colors import *
# Known numbers:
print(f"pi number: {PI}")
print(f"euler number: {EULER}")
print(f"golden ratio number: {GOLDEN_RATIO}")
print(f"kaprekar number: {KAPREKAR}")

# Coordinates
coordenate = Coordinates(10, -10)
p = Coordinates(-10, 10)
print(coordenate - p) # Returns another coordinate with the subtraction / adding (coordenate + p)

# Color
color = Color("#911B1B")
randomcolor = randomColor() # Creates a random color
print(randomcolor)
# Roman:
roman_Number = Roman("XVII")
print(roman_Number.RomanToDec()) # 17
any_number = 10
print(DecToRoman(any_number)) # X

# Primes:
prime = 17
print(is_prime(prime, [2, 3, 5])) # True (means it's prime)
# The [2, 3, 5] list is another thing which you need to put in there (those are numbers minor than the prime you're checking)
print(generate_primes(40)) # Will generate prime numbers until the parameter you put (must be int) [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
# print(decompose(120)) # Will do a factorial decompose with the number you passed (may take a while)
print(mcm(12, 24)) # Returns the answer to the mcm
print(mcd(12, 24)) # Same as mcm but different operation


# Segments (matplotlib)
segment = Segments([(10, -10), (50, -10), (0, 10)])
#segment.draw(color=color)

rectangle = Rectangles(12, 24)
rectangle.draw()