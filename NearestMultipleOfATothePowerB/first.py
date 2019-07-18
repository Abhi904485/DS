import math


def nearest_multiple(x, a, b):
    if b < 0:
        return 0
    mul = a**b
    temp_ans = mul // x
    ans1 = x * temp_ans
    ans2 = x * (temp_ans + 1)
    return ans1 if abs(ans1 - mul) <= abs(mul - ans2) else ans2


x, a, b = tuple(map(int, input().split(" ")))
print(nearest_multiple(x ,a, b))
