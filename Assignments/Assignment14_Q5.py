''''Write a lambda function which accepts one number and 
returns True if number is even otherwise False.'''

even = lambda x : (x % 2 == 0)

def main():
    no = int(input("Enter number : "))
    if(even(no)):
        print("Even number")
    else:
        print("not even number")

if __name__ == "__main__":
    main()