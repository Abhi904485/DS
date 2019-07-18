a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def bubble_sort():
    for i in range(len(a)-1, 0, -1):
        for j in range(i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


bubble_sort()
print(a)
