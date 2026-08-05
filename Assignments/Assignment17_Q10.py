'''Write a program which accept number from user and 
return addition of digits in that number.
Input : 5187934                Output : 37'''


def sumDigits(num):
    sum = 0
    while num>0:
        sum = sum + (num%10)
        num = num//10
    return sum

def main():
    num = int((input("enter number : ")))
    result = sumDigits(num)
    print("Sum of digits:", result)

if __name__ == "__main__":
    main()