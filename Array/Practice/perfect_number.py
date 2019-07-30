import math


def printAl(n):
    sum_ = 1
    i =2
    while i < math.sqrt(n):
        if n % i == 0:
            sum_ += i + n // i
        i+=1
    if sum_ == n:
        print(1, end=" ")

    else:
        print(0, end=" ")


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        printAl(n)
        print()
