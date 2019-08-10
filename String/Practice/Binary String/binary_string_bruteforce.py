def printAl(string):
    count = 0
    for i in range(len(string)):
        if string[i].startswith("1"):
            for j in range(i+1, len(string)):
                if string[j] == '1':
                    count += 1
                else:
                    continue
    print(count)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        str_length = int(input())
        string = str(input())
        printAl(string)
