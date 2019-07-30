def maxsumarray(a, length):
    maxsumsofar = a[0]
    currentmaxsum = a[0]
    for i in range(1, length):
        currentmaxsum = max(a[i], currentmaxsum + a[i])
        maxsumsofar = max(currentmaxsum, maxsumsofar)
    return maxsumsofar


array = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum Contiguous Sum is ", maxsumarray(array, len(array)))

# well optimized method using pythons max function
