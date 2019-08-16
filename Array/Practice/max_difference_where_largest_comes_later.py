def max_difference_between_element(arr, n):
    max_diff_so_far = -1
    min_element = arr[0]
    for i in range(1, n):
        temp = arr[i] - min_element
        if temp > max_diff_so_far:
            max_diff_so_far = temp
        if arr[i] < min_element:
            min_element = arr[i]
    return max_diff_so_far


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(max_difference_between_element(arr, n))
