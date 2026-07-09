'''Write a lambda function which accepts two numbers and returns maximum number.'''

max = lambda x,y : x if x>y else y

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    print(f"Maximum number is : {max(no1, no2)}")

if __name__ == "__main__":
    main()