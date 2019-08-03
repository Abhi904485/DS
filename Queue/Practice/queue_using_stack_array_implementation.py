
stack_1 = []
stack_2 = []


def enqueue(x):
    global stack_1
    stack_1.append(x)


def dequeue():
    global stack_1
    global stack_2
    if len(stack_1) == 0:
        return - 1
    else:
        if len(stack_1) == 1:
            return stack_1.pop(0)
        while len(stack_1) != 0:
            stack_2.append(stack_1.pop(0))
        tmp = stack_2.pop(0)
        stack_1 = stack_2[:]
        return tmp


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                enqueue(a[i+1])
                i += 1
            else:
                print(dequeue(), end=" ")
            i += 1
        stack_1 = []
        stack_2 = []
        print()
