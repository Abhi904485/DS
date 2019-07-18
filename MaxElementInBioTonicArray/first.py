def printAl(arr, n, x):
    for i in range(n):
        if x == arr[i]:
            print(i, end=" ")
            break
    else:
        print(-1, end=" ")


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x = int(input())
        printAl(arr, n, x)
        print()
