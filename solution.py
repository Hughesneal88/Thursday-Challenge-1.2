def solution():
    n= input("Enter a number: ")
    n = n.strip(" ")

    if n == n[::-1]:
        print(True)
    else:
        print(False)

if __name__ == '__main__':
    solution()