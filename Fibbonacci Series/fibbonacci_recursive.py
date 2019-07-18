def fibbo(number):
    x, y = 0, 1
    if number<0:
        pass
    else:
        if number is x:
            return x
        elif number is y:
            return y
        else:
            return fibbo(number-1) + fibbo(number-2)
print(fibbo(10))
