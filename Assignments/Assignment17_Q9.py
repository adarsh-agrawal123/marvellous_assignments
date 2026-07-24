'''Write a program which accept number from user and return number of digits in that number.
Input : 5187934                Output : 7'''


def main():
    no = int(input("Enter number : "))

    print("Number of digits are : ",len(str(no)))

if __name__ == "__main__":
    main()