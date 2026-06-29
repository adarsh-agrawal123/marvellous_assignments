'''Write a program which accepts one number 
and prints square of that number.Input: 5Output: 25'''

def square(No):
    return No*No

def main():
    No = int(input("Enter number : "))
    Ans = square(No)
    print("The square is : ",Ans)

if __name__ == "__main__":
    main()