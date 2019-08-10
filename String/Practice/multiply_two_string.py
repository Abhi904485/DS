def multiply(a, b):
    print(int(a)*int(b))


if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a, b = input().split()
        multiply(a, b)
