# O(1) approach


def printAl(lis: list, n):
    if(n == 1):
        print(lis[0])
    elif(n % 2 == 1):
        ind = int((n - 3) / 4) + 3
        return lis[ind - 1]
    else:
        ind = int((n - 2) / 4) + 2
        return lis[ind - 1]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(printAl(arr, n), end=" ")
        print()
