
queue_1 = []
queue_2 = []


def push_in_stack(x):
    global queue_1
    queue_1.append(x)


def pop_from_stack():
    global queue_1
    global queue_2
    if len(queue_1) == 0:
        return - 1
    else:
        if len(queue_1) == 1:
            return queue_1.pop()
        while len(queue_1) > 1:
            queue_2.append(queue_1.pop(0))
        tmp = queue_1[0]
        queue_1 = queue_2[:]
        queue_2.clear()
        return tmp



if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        i = 0
        while i < len(a):
            if a[i] == 1:
                push_in_stack(a[i+1])
                i += 1
            else:
                print(pop_from_stack(), end=" ")
            i += 1
        queue_1 = []
        queue_2 = []
        print()
