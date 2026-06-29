'''Write a program which accepts one number and checks whether it is divisible by 3 and 5'''

def divisible(No):
    if(No % 3 == 0 and No % 5 == 0):
        return True
    else:
        return False
    
def main():
    No = int(input("Enter number : "))
    Ans = divisible(No)
    if(Ans == True):
        print("Divisible by 3 & 5")
    else:
        print("Not divisible by 3 & 5")

if __name__ == "__main__":
    main()