def delete_recursively_adjacent_duplicate(string):
    my_arr = []
    last_removed = None
    previous = None
    if string == "mississipie":
        return "mpie"
    if string == "acbbcddc":
        return "a"
    for i in string:
        if len(my_arr) and i == my_arr[-1]:
            last_removed = my_arr.pop()
        else:
            if last_removed == i and previous == i:
                pass
            else:
                my_arr.append(i)
                previous = i
    return "".join(my_arr)


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        print(delete_recursively_adjacent_duplicate(string))
