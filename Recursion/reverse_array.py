my_list = []


def iterate_reverse(arr):
    if len(arr) == 1:
        return str(arr[0])
    return iterate_reverse(arr[1:]) + " " + str(arr[0])


if __name__ == "__main__":
    arr = [1, 2]
    print(list(map(int, iterate_reverse(arr).split())))
