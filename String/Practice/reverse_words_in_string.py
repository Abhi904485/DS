def printAl(string):
    result = ""
    l = reversed(string.split("."))
    result += ".".join(l)
    print(result)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        printAl(string)
