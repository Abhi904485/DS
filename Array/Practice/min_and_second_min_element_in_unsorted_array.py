def find_min_and_second_min_element(arr, n):
    first_min = arr[0]
    second_min = None
    for i in range(1, n):
        if arr[i] < first_min:
            second_min = first_min
            first_min = arr[i]
        else:
            if not second_min and arr[i] > first_min:
                second_min = arr[i]
            if arr[i] > first_min and arr[i] < second_min:
                second_min = arr[i]

    return (first_min, second_min) if second_min else -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        res = find_min_and_second_min_element(arr, n)
        if isinstance(res, tuple):
            print("{} {}".format(res[0], res[1]))
        else:
            print(res)
