def reverse_string(string):
    if len(string) < 2:
        return string

    return reverse_string(string[1:]) + string[0]


print(reverse_string("abcd"))