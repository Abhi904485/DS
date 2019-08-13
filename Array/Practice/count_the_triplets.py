def count_the_triplets(arr, n):
    count = 0
    arr.sort()
    arr_set = set(arr)
    max_ = arr[-1]
    for i in range(n-1):
        for k in range(i+1, n):
            item = arr[i]+arr[k]
            if item > max_:
                break
            if item in arr_set:
                count += 1
    return count if count >0 else -1


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(count_the_triplets(arr, n))
