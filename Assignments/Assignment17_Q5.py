'''Write a program which accept one number for user and check whether number 
is prime or not.
Input : 5          Output : It is Prime Number'''


def ChkPrime(no):
    for i in range(2, no):
        if(no % i == 0):
            return False
        
    return True

def main():
    no = int(input("Enter number : "))

    if(ChkPrime(no)):
        print("It is prime number")
    else:
        print("Not prime")

if __name__ == "__main__":
    main()