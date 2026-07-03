'''Write a program which accepts one number and 
checks whether it is prime or not.Input: 11 Output: Prime Number'''


def prime(no):
    for i in range(2,no):
        if(no % i == 0):
            return "not prime"
        
    return "prime number"

def main():
    no = int(input("Enter number : "))
    Ans = prime(no)
    print("Result : ",Ans)

if __name__ == "__main__":
    main()