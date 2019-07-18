def string_reverse(string):
    if len(string) == 0:
        return string
    else:
        return string_reverse(string[1:len(string)]) + string[0]


print(string_reverse("Abhishek"))
