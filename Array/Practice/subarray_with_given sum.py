def subarray_with_given_sum(arr, n, sum_):
    wsum = 0
    start = 0
    for i in range(n):
        if wsum < sum_:
            wsum += arr[i]
        while wsum > sum_:
            wsum -= arr[start]
            start += 1
        if wsum == sum_:
            return start + 1, i + 1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, sum_ = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        if isinstance(subarray_with_given_sum(arr, n, sum_), tuple):
            start, end = subarray_with_given_sum(arr, n, sum_)
            print("{} {}".format(start, end))
        else:
            print(-1)
