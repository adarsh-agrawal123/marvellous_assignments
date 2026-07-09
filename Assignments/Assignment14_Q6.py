'''Write a lambda function which accepts one number and 
returns True if number is odd otherwise False.'''

odd = lambda x : (x % 2 != 0)

def main():
    no = int(input("Enter number :"))
    if(odd(no)):
        print("Odd number")
    else:
        print("not odd number")

if __name__ == "__main__":
    main()