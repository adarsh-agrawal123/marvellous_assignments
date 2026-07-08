'''Write a program which accepts one number and 
prints factorial of that number.Input: 5 Output: 120'''


def factorial(no):
    ans = 1
    for i in range(1,no+1):
        ans = ans * i

    return ans

def main():
    no = int(input("Enter number : "))
    ans = factorial(no)
    print("result : ",ans)

if __name__ == "__main__":
    main()