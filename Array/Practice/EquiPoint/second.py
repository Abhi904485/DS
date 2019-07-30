def printAl(a, n):
    sum_ = sum(a)
    left_sum_ = 0
    if len(a) == 1:
        print(1, end=" ")
    else:
        for i in range(n):
            sum_ -= a[i]
            if sum_ == left_sum_:
                print(i + 1, end=" ")
                break
            left_sum_ += a[i]
        else:
            print(-1, end=" ")


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        printAl(arr, n)
        print()

# this is the O(n) appraoch
