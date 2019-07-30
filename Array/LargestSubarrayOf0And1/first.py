def largest_subarray_0_1(arr: list, n):
    my_list = []
    max_my_list = []
    for i in arr:
        if i == 0:
            my_list.append(-1)
        else:
            my_list.append(i)
    print(my_list)
    sum_ =100
    for i in range(n):
        sum_ += my_list[i]
        max_result = 0
        for j in range(i + 1, n):
            sum_ += my_list[j]
            if sum_ == 100 and j > max_result:
                max_result = j - i + 1
                max_my_list.append(max_result)
        sum_ = 100
    return max(max_result)


if __name__ == '__main__':
    testcase = int(input())
    for test in range(testcase):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(largest_subarray_0_1(arr, n))
        print()
