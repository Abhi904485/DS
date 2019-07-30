import math


def fibbonaci_constant(n):
    fib_list = []
    phi = (1 + math.sqrt(5)) / 2
    for i in range(n):
        fib_list.append(round(pow(phi, i)/math.sqrt(5)))
    return fib_list


if __name__ == "__main__":
    print(fibbonaci_constant(10))
