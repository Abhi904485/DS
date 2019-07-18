# this is for negative number .
# T(n) = O(log(n))
# S(n) = O(1)


def cal_power(x, y):
    res = 1
    while y:
        if y & 1:
            res *= x
        x *= x
        y >>= 1

    return res


print(cal_power(3, 3))
