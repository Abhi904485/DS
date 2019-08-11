def delete_consecutive_elements_more_than_once(string):
    arr = []
    for i in string:
        if len(arr) and arr[-1] == i:
            pass
        else:
            arr.append(i)
    return "".join(arr)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        print(delete_consecutive_elements_more_than_once(string))
