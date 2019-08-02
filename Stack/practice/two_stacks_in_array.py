def pop1(a):
    return a.pop(0)


def push1(a, x):
    a.insert(0, x)


def pop2(a):
    return a.pop()


def push2(a, x):
    a.append(x)


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        a = [-1 for i in range(101)]  # array to be used for the 2 stacks.
        i = 0  # curr index
        while i < len(arr):
            if arr[i] == 1:
                if arr[i+1] == 1:
                    push1(a, arr[i+2])
                    i += 1
                else:
                    print(pop1(a), end=" ")
                i += 1
            else:
                if arr[i+1] == 1:
                    push2(a, arr[i+2])
                    i += 1
                else:
                    print(pop2(a), end=" ")
                i += 1
            i += 1
