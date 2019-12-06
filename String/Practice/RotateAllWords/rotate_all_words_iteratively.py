def rotate_string(input_string):
    count = 0
    while count <= len(input_string):
        print(f"{input_string}")
        input_string = input_string[1:]+input_string[0]
        count += 1


if __name__ == "__main__":
    rotate_string("Abhishek")
