def is_prime(a, minor_primes): # For decimals
  for p in minor_primes:
    #print(f'{n} y {p}')
    if a % p == 0:
      return False
  return True

# Example:
# is_prime(7, [2, 3, 5]) # True
# is_prime(15, [2, 3, 5, 7, 11, 13])  # False


def generate_primes(until):
    primes = []
    for i in range(2, until):
        if is_prime(i, primes) == True:
            primes.append(i)
    return primes

def decompose(a):
    l = generate_primes(a)
    elements_factor_exponent = {}
    for c in l:
        while a % c == 0:
            if c in elements_factor_exponent:
                elements_factor_exponent[c] += 1
            else:
                elements_factor_exponent[c] = 1
        a = a//c
    return elements_factor_exponent

# decompose(8*9*5*11)  # {2: 3, 3: 2, 5: 1, 11: 1}

def print_descom(d, mult='·'):
    sir = [f"{k}^{v}" for k, v in d.items()]
    return f" {mult} ".join(sir)

# print_descom(descompose(8*9*5*11))
# print_descom(decompose(8*9*5*11), mult='*') # Change symbol

def mcm(a, b):
    a, b = abs(a), abs(b)
    mcd_value = mcd(a, b)
    return abs(a * b) // mcd_value

def mcd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        a, b = b, a % b
    return a
