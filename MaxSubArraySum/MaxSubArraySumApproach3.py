import sys


def maxarraysum(a, size):
    maxsofar = -sys.maxsize
    currentmaxvalue = 0
    for i in range(0, size):
        currentmaxvalue = currentmaxvalue + array[i]
        if maxsofar < currentmaxvalue:
            maxsofar = currentmaxvalue
        if currentmaxvalue < 0:
            currentmaxvalue = 0
    return maxsofar


array = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Max Array Sum", maxarraysum(array, len(array)))
# original method
