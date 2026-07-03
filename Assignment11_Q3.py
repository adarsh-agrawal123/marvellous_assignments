'''Write a program which accepts one number and 
prints sum of digits.Input: 123 Output: 6'''

def sum(no):
    ans = 0
    while no > 0:
        rem = no % 10
        ans = ans + rem
        no = no // 10

    return ans
    
def main():
    no = int(input("Enter number :"))
    ans = sum(no)
    print("result : ",ans)

if __name__ == "__main__":
    main()