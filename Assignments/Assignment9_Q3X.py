'''Write a program which accepts one number 
and prints square of that number.Input: 5Output: 25'''

#lambda function
square = lambda No : No*No

def main():
    No = int(input("enter number : "))
    Ans = square(No)
    print("square is : ",Ans)

if __name__ == "__main__":
    main()