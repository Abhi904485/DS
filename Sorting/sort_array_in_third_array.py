a = [11, 12, 13, 14, 15, 16, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


def merge_array(a, l1, l2, u1, u2):
    i = l1
    j = l2
    k = 0
    while i <= u1 and j <= u2:
        if a[i] < a[j]:
            temp[k] = a[i]
            i += 1

        else:
            temp[k] = a[j]
            j += 1
        k += 1

    while i <= u1:
        temp[k] = a[i]
        i += 1
        k += 1

    while j <= u2:
        temp[k] = a[j]
        j += 1
        k += 1


l1 = 0
l2 = 6
u1 = 5
u2 = 15
temp = [0] * ((u2 - l2 + 1) + (u1 - l1 + 1))
merge_array(a, l1, l2, u1, u2)
print(temp)
