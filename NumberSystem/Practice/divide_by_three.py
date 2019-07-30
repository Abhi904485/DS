def printAl(n):
    sum_ = 0
    number = str(int(str(n), 2))
    for i in number:
        sum_ += int(i)
    if sum_ % 3 == 0:
        return 1
    return 0


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(printAl(n))
