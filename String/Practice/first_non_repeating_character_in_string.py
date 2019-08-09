from collections import OrderedDict


def printAl(string: str, n: int):
    char = OrderedDict()
    for i in string:
        if i not in char:
            char[i] = [i, 1]
        else:
            char[i][1] += 1
    for i in char.values():
        if i[1] == 1:
            print(i[0])
            break
    else:
        print(-1)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        string = str(input())
        printAl(string, n)
