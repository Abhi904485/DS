def my_factorial(number):
    if number == 0 or number == 1:
        return 1
    return number*my_factorial(number-1)


if __name__ == "__main__":
    print(my_factorial(int(input("Enter the numnber: "))))
