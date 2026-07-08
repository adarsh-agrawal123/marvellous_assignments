'''Write a program which accepts one number and 
checks whether it is palindrome or not.Input: 121 Output: Palindrome Number'''

def chkPalindrome(num):
    temp = 0
    while num>0:
        temp = temp * 10
        temp = temp + (num % 10)
        num = num // 10

    return temp


def main():
    no = int(input("Enter number : "))

    if(no == chkPalindrome(no)):
        print("Palindrome")
    else:
        print("not palindrome")

if __name__ == "__main__":
    main()