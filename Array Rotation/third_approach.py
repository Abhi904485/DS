arr = [1, 2, 3, 4, 5, 6, 7]
d = 3
# first Reverse 0 to d elements arr[d - 1::-1]
# second reverse d+1 to len(arr) elements
# then reverse total elements
arr = arr[d - 1::-1] + arr[:d:-1]
print(arr[::-1])
