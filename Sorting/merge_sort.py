a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def merge(a, temp, l1, u1, l2, u2):
    i = l1
    j = l2
    k = l1
    while i <= u1 and j <= u2:
        if a[i] <= a[j]:
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


def copy(a, temp, start, end):
    for i in range(start, end + 1):
        a[i] = temp[i]


def sort(a, temp, start, end):
    if start == end:
        return
    mid = (start + end) // 2
    sort(a, temp, start, mid)
    sort(a, temp, mid + 1, end)
    merge(a, temp, start, mid, mid + 1, end)
    copy(a, temp, start, end)


def merge_sort(a):
    n = len(a)
    temp = [None] * n
    sort(a, temp, 0, n - 1)


merge_sort(a)
print(a)
