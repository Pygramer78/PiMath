# Hello and Welcome!
## About this repository 👀
Pygramer78, created this library in june 2025, with the idea of educational programming implemented to python. \
Since i thought of this proyect, i made many stuff, like roman numbers, and all of that. \
After all, i ended up using a lot of my time making this. \
I hope you like it!
# Instructions
Just read the example file. \
Or i'll show it to you now. \
```
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
print(coordenate - p) # Returns another coordinate with the subtraction / adding (coordenate + p)

# Color
color = Color("#911B1B")

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
print(decompose(120)) # Will do a factorial decompose with the number you passed (may take a while)
print(mcm(12, 24)) # Returns the answer to the mcm
print(mcd(12, 24)) # Same as mcm but different operation


# Segments (matplotlib)
segment = Segments([(10, -10), (50, -10)])
segment.draw(color=color)

```
