def find_max_and_second_max_element(arr):
    first_max = arr[0]
    second_max = None
    for i in range(1, len(arr)):
        if arr[i] > first_max:
            second_max = first_max
            first_max = arr[i]
        else:
            if not second_max and arr[i] < first_max:
                second_max = arr[i]
            if arr[i] < first_max and arr[i] > second_max:
                second_max = arr[i]

    return second_max if second_max else -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        arr = list(map(int, input().split()))
        print(find_max_and_second_max_element(arr))
