import math


def nearestPower(a, b):
    if b < 0:
        return 0
    x = math.floor(math.log(b, a))
    xPlusOne = x + 1
    number1 = a**x
    number2 = a**xPlusOne
    return number2 if abs(number1 - b) > abs(number2 - b) else number1


print(nearestPower(4, 63))
