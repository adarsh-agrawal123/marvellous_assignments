'''Write a program which accepts one number and 
prints sum of first N natural numbers.Input: 5 Output: 15'''

def sum(no):
    ans = 0
    for i in range(no+1):
        ans = ans + i

    return ans

def main():
    no = int(input("Enter number : "))
    ans = sum(no)
    print("result : ",ans)

if __name__ == "__main__":
    main()