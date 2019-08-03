stack = []


def push_in_stack(x):
    stack.append(x)


def pop_from_stack():
    if len(stack) == 0:
        return - 1
    return stack.pop()


def min_element_from_stack():
    if len(stack) == 0:
        return -1
    return min(stack)


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
            elif a[i] == 2:
                print(pop_from_stack(), end=" ")
            else:
                print(min_element_from_stack(), end=" ")
            i += 1
        print()
