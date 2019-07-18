a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
for i in range(len(a) - 1):
    min_index = i
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            min_index = j

    if min_index != i:
        a[i], a[min_index] = a[min_index], a[i]
print(a)