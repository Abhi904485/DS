def minDist(a, n, x, y):
    if (str(x) in a) and (str(y) in a):
        no_of_x = []
        no_of_y = []
        for i in range(n):
            if str(x) == a[i]:
                no_of_x.append(i)
            if str(y) == a[i]:
                no_of_y.append(i)
        final = []
        for i in no_of_x:
            for j in no_of_y:
                final.append(abs(i - j))
        return min(final)

    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        x = int(input())
        y = int(input())
        print(minDist(arr, n, x, y), end=" ")
        print()
