def findmaxarraysum(a, size):
    currentmax = 0
    finalsum = 0
    for i in range(0, size):
        currentmax = currentmax + array[i]
        if currentmax < 0:
            currentmax = 0
        elif finalsum < currentmax:
            finalsum = currentmax
    return finalsum

array = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum sub array sum ", findmaxarraysum(array, len(array)))

# In this when current max is greator than 0 then only it change the value of final sum
