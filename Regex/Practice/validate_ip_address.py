def is_valid(ip_address: str):
    my_list = ip_address.split(".")
    if len(my_list) == 4:
        for i in my_list:
            if int(i) > 255:
                return 0
            else:
                return 1
    else:
        return 0


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        ip_address = str(input())
        print(is_valid(ip_address))
