def printAl(string, last_removed):
    if len(string) == 1 or len(string) == 0:
        return string

    if string[0] == string[1]:
        last_removed = ord(string[0])
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]

        return printAl(string, last_removed)
    rem_str = printAl(string[1:], last_removed)
    print(rem_str)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        final = []
        n = str(input())
        printAl(n, last_removed=0)
        print()
