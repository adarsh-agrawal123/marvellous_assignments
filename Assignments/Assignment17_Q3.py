'''Write a program which accept one number from user and return its factorial.
Input :       5                 Output : 120'''


def factorial(no):
    ans = 1
    for i in range(2, no+1):
        ans = ans * i

    return ans

def main():
    no = int(input("Enter number : "))
    ret = factorial(no)
    print(f"Factorial is : {ret}")

if __name__ == "__main__":
    main()