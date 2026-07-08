'''Write a program which accepts one number and prints cube of that number'''

cube = lambda No : No*No*No
def main():
    No = int(input("Enter number : "))
    Ans = cube(No)
    print("cube is :",Ans)

if __name__ == "__main__":
    main()