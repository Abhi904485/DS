my_list = []


def iterate_reverse(arr):
    if len(arr) == 1:
        return arr[0]
    return iterate_reverse(arr[1:]) + arr[0]


if __name__ == "__main__":
    arr = [1, 2]
    print(iterate_reverse(arr))
