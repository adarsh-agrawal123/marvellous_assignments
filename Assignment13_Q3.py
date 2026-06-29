'''Write a program which accepts one number and checks 
whether it is perfect number or not.Input: 6 Output: Perfect Number'''

def perfect(No):
    if(No % 2 == 0 and No % 3 == 0):
        return True
    else:
        return False
    
def main():
    No = float(input("Enter number : "))
    Ans = perfect(No)
    if(Ans == True):
        print("perfect number")
    else:
        print("not perfect number")

if __name__ == "__main__":
    main()