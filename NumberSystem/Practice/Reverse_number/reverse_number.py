def custom_reverse(num):
    sum_ = 0 
    while num > 0:
        temp = num % 10
        sum_  = sum_*10 + temp
        num  = num //10
    return sum_


print(custom_reverse(1202))
