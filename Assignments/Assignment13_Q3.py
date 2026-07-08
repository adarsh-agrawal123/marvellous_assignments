'''Write a program which accepts one number and checks 
whether it is perfect number or not.Input: 6 Output: Perfect Number'''

def perfect(No):
    sum = 0
    for i in range(1, No):
        if(No % i == 0):
            sum = sum + i
    
    return sum
    
def main():
    No = int(input("Enter number : "))
    Ans = perfect(No)
    if(Ans == No):
        print("perfect number")
    else:
        print("not perfect number")

if __name__ == "__main__":
    main()