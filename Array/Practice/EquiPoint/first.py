# code
def equi_point(a, n):
    if n == 1:
        print(1, end=" ")
    else:
        for i in range(n):
            sum1 = sum(a[0:i + 1])
            sum2 = sum(a[i + 2:])
            if sum1 == sum2:
                print(i + 2, end=" ")
                break
        else:
            print(-1, end= " ")


equi_point([1], 1)



# T(O) = O(n^2)