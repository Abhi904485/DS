import sys
def rotate_string(input_string, count=0):
    if count == len(input_string)+1:
        sys.exit(0)
    print(input_string)
    rotate_string(input_string[1:]+input_string[0],count+1)



if __name__ == "__main__":
    rotate_string("Abhishek")
