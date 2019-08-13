a = [119, 160, 390, 947, 604, 251 ]
for i in range(len(a) - 1):
    min_index = i
    for j in range(i + 1, len(a)):
        if a[j] < a[i]:
            min_index = j
        a[i], a[min_index] = a[min_index], a[i]
print(a)