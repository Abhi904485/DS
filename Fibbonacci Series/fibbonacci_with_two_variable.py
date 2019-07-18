#iterative Approach
def fibbonaci(num):
    a, b, count = 0, 1, 0
    if num < 0:
        print("Not Applicable")
    while count < num:
        print(a)
        a, b = b, a + b
        count += 1


fibbonaci(9)
# T(n) = O(n)
# S(n) =O(1)