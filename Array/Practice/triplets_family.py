def triplet_family(arr, n):
    count = 0
    arr.sort()
    arr_set = set(arr)
    max_ = arr[-1]
    f = 0
    for i in range(n-1):
        if f == 0:
            for k in range(i+1, n):
                item = arr[i]+arr[k]
                if item > max_:
                    break
                if item in arr_set:
                    count += 1
                    f = 1
                    break
        else:
            return [0, 0, 0] if count > 0 else []
    else:
        return []


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(triplet_family(arr, n))
