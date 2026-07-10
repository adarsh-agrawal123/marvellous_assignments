'''Write a lambda function which accepts two numbers and returns multiplication'''

multiplication = lambda x,y : x*y

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    print("Multiplication is : ", multiplication(no1, no2))

if __name__ == "__main__":
    main()