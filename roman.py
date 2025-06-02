class Roman:
    def __init__(self, number: str):
        self.number = number
    def __repr__(self):
        return f"Number: {self.number}"
    def RomanToDec(self):
        numbers = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
        }
        total = 0
        itemb = 0
        n = reversed(self.number.upper())
        for i in n:
            value = numbers[i]
            if value < itemb:
                total -= value
            else:
                total += value
                itemb = value
        return total

def DecToRoman(number):
    values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, symbol in values:
        while number >= value:
            result += symbol
            number -= value
    return result
