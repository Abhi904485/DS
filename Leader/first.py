def printAl(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>=arr[j]:
                if j == n-1:
                    print(arr[i], end= " ")
                continue
            else:
                break
            
    print(arr[-1], end= " ")

#  this is o(n^2) approach 