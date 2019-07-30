my_list = []
from itertools import permutations

def permutation(string, step=0):
    if step == len(string):
        my_list.append(int("".join(string)))
    for i in range(step, len(string)):
        arr = list(string)
        arr[step], arr[i] = arr[i], arr[step]
        permutation(arr, step=step + 1)


def printAl(n):
    permutation(str(n))
    new_set  = set(my_list)
    new_list = sorted(new_set)
    max_ = max(new_list)
    if n == max_:
        return "not possible"
    else:
        index = new_list.index(n)
        return new_list[index+1]


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        my_list = []
        n = int(input())
        print(printAl(n), end=" ")
        print()
