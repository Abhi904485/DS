a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
n = len(a)
jump_value_list = [0]
while (3 * jump_value_list[0] + 1) < len(a):
    jump_value_list.insert(0, 3 * jump_value_list[0] + 1)

for jump_value in (value for value in jump_value_list if value > 0):
    for i in range(jump_value, len(a)):
        temp = a[i]
        j = i - jump_value
        while j >= 0 and temp < a[j]:
            a[j + jump_value] = a[j]
            j -= jump_value
        a[j + jump_value] = temp

print(a)
print(jump_value_list)
