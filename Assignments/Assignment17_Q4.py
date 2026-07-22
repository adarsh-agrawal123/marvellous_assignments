'''Write a program which accept one number form user and return addition of its factors.
Input :       12                Output : 16(1+2+3+4+6)'''


def factors(no):
    ans = 0

    for i in range(1, no):
        if(no % i == 0):
            ans = ans + i

    return ans

def main():
    no = int(input("Enter number : "))

    ret = factors(no)

    print("Output : ",ret)

if __name__ == "__main__":
    main()