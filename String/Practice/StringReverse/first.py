my_str = "Abhis"

my_str_list = list(my_str)

for i in range(len(my_str)//2):
    my_str_list[i], my_str_list[len(my_str) - i - 1] = my_str_list[len(my_str) - i - 1], my_str_list[i]

x = "".join(my_str_list)

print(x)
print("Abhishek")