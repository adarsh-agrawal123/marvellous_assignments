'''Write a lambda function which accepts one number and returns True if divisible by 5.'''

divisible = lambda x : (x % 5 == 0)

def main():
    no = int(input("Enter number : "))
    if(divisible(no)):
        print("divisible by 5")
    else:
        print("not divisible by 5")

if __name__ == "__main__":
    main()