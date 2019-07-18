a2 = [1, 2, 3, 4, 5, 6]
a1 = [11, 12, 13, 14, 15, 16]
temp = [0] * (len(a1) + len(a2))
i = 0
j = 0
k = 0
while i <= len(a1) - 1 and j <= len(a2) - 1:
    if a1[i] < a2[j]:
        temp[k] = a1[i]
        i += 1
    else:
        temp[k] = a2[j]
        j += 1
    k += 1
while i <= len(a1)-1:
    temp[k] = a1[i]
    i += 1
    k += 1

while j <= len(a2)-1:
    temp[k] = a2[j]
    j += 1
    k += 1

print(temp)
