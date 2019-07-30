import sys


def hourglassSum(arr):
    max_ = -sys.maxsize
    for i in range(4):
        for j in range(4):
            sum_ = 0
            sum_ += arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + \
                arr[i + 1][j + 1] + \
                arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            if sum_ > max_:
                max_ = sum_
    return max_


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(hourglassSum(arr))
