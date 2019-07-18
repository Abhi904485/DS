# this is for positive number .
# T(n) = O(log(n))
# S(n) = O(1)


def cal_power(x, y):
    if not y:
        return 1
    # recursion and saving previous value for next iteration DP
    temp = cal_power(x, int(y / 2))
    if y % 2 == 0:
        return temp * temp
    else:
        return x * temp * temp


print(cal_power(2, 3))
