def push(arr, ele):
    arr.append(ele)


def pop(arr):
    if not isEmpty(arr):
        return arr.pop()


def isFull(n, arr):
    if len(arr) == n:
        return True
    return False


def isEmpty(arr):
    if len(arr) == 0:
        return True
    return False


def getMin(n, arr):
    return min(arr)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        stack = []
        for i in range(n):
            push(stack, arr[i])
        print(getMin(n, stack))
