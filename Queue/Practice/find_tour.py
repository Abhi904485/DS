def tour(lis, n):
    size = len(lis)
    for i in range(size):
        lis[i] = lis[i][0] - lis[i][1]
    sum_ = 0
    for i in range(size):
        index = i
        start = index
        while i < size + index:
            sum_ += lis[i % size]
            if sum_ < 0:
                sum_ = 0
                break
            i += 1
            if i % size == start and sum_ >= 0:
                return i % size
    else:
        return -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = []
        for i in range(1, 2*n, 2):
            lis.append([arr[i-1], arr[i]])
        print(tour(lis, n))
