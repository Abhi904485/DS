def printAl(string):
    count = 0
    for i in string:
        if i == '1':
            count += 1
    print(count*(count-1)//2)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str_length = int(input())
        string = str(input())
        printAl(string)
