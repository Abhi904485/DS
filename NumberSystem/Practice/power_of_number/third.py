# this is for negative number .
# T(n) = O(log(n))
# S(n) = O(1)

def cal_power(x, y):
    if not y:
        return 1
    #recursion and saving previous value for next iteration DP    
    temp = cal_power(x, int(y / 2))
    if y % 2 == 0:
        return temp * temp
    elif y>0:
        return x * temp * temp
    else:
        return (temp*temp)/x


print(cal_power(3, -3))


