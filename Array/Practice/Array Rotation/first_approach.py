arr = [1, 2, 3, 4, 5, 6, 7]
d = 2
temp = []
for i in range(d):
    temp.append(arr[i - i])
    arr.remove(arr[i - i])
    arr.append(temp[i])
print(arr)
