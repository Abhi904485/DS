import sys


def kadanes(arr, n):
    max_so_far = -sys.maxsize
    current_max_value = 0
    for i in range(n):
        current_max_value += arr[i]
        if max_so_far < current_max_value:
            max_so_far = current_max_value
        if max_so_far < 0:
            return 0
        return max_so_far


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(kadanes(arr, n))
