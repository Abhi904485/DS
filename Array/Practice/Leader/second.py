def printAl(arr,n):
    max = float('-inf')
    my_list = []
    for i in range(n-1,-1,-1):
        if max<= arr[i]:
            max  = arr[i]
            my_list.append(max)
    for j in range(len(my_list)-1, -1, -1):
        print(my_list[j],end =" ")
            
        
                

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        printAl(arr,n)
        print()

# O(n) approach