import sys


def contiguous_subarray_min_average(arr, n, k):
    average_ = sys.maxsize
    start = end = None
    for i in range(n-k+1):
        if average_ > sum(arr[i: i + k])/k:
            start = i+1
            average_ = sum(arr[i: i + k])/k
            end = i+k
    return start, end


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n, k = list(map(int, input().split()))
        arr = list(map(int, input().split()))
        start, end = contiguous_subarray_min_average(arr, n, k)
        print("{} {}".format(start, end))
