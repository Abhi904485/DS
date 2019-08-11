def delete_recursively_adjacent_duplicate(string, removed_last=None):
    if len(string) == 1 or len(string) == 0:
        return string

    if string[0] == string[1]:
        removed_last = string[0]
        while len(string) > 1 and string[0] == string[1]:
            string = string[1:]
        string = string[1:]
        return delete_recursively_adjacent_duplicate(string, removed_last)

    rem_str = delete_recursively_adjacent_duplicate(string[1:], removed_last)

    if len(rem_str) and string[0] == rem_str[0]:
        return rem_str[1:]
    if not len(rem_str) and removed_last == string[0]:
        return rem_str
    else:
        return string[0] + rem_str


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        string = str(input())
        print(delete_recursively_adjacent_duplicate(string))
