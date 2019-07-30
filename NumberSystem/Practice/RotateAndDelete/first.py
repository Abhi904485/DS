# o(n) approach


def printAl(arr, n):
    count = 1
    if len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return arr[1]
    else:
        while len(arr) > 1:
            temp = arr.pop()
            arr.insert(0, temp)
            if len(arr) > count:
                del arr[len(arr) - count]
            else:
                return arr[1]
            count += 1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(printAl(arr, n), end=" ")
        print()
