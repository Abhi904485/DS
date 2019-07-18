# this is for positive number .
# T(n) = O(n)
# S(n) = O(1)
# no of activation record = O(log(n))


def cal_power(x, y):

    if not y:
        return 1
    elif y % 2 == 0:
        # recursion , divide and conquer
        return cal_power(x, int(y / 2)) * cal_power(x, int(y / 2))
    else:
        return x * cal_power(x, int(y / 2)) * cal_power(x, int(y / 2))


print(cal_power(2, 3))
