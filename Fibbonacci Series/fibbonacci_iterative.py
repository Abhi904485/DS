def fibbo(number):
    x, y = 0, 1
    print(x, end=" ")
    print(y, end=" ")
    for i in range(number):
        z = x+y
        x = y
        y = z
        print(z, end=" ")
fibbo(10)
