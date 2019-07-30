my_list = []
def printAl(n,step=0):
    if step == len(n):
        my_list.append("".join(n))
    for i in range(step,len(n)):
        arr = list(n)
        arr[step],arr[i] = arr[i],arr[step]
        printAl(arr,step=step+1)
    
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=str(input())
        printAl(n)
        my_list.sort()
        print(" ".join(my_list),sep=" ",end=" ")
        print()
        my_list.clear()