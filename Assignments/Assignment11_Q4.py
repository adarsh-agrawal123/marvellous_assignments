'''Write a program which accepts one number and 
prints reverse of that number.Input: 123 Output: 321'''


def reverse(no):
    ans = 0
    while no > 0:
        ans = ans * 10
        ans = ans + (no % 10)
        no = no // 10

    return ans

def main():
    no = int(input("Enter number : "))
    ans = reverse(no)
    print("Reversed number : ",ans)

if __name__ == "__main__":
    main()