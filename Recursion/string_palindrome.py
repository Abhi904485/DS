def palindrome(string):
    if len(string) == 0:
        return string
    return palindrome(string[1:]) + string[0]


if __name__ == "__main__":
    print("Yes" if palindrome("aba") == "aba" else "NO")
