'''Write a program which accepts one number and 
prints count of digits in that number.Input: 7521 Output: 4'''


def count(no):
    no = str(no)
    return len(str(no))

def main():
    no = int(input("enter number : "))
    ans = count(no)
    print("Result : ",ans)

if __name__ == "__main__":
    main()