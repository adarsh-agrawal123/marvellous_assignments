'''Write a program which contains one function named as Add() which accepts two numbers 
from user and return addition of that two numbers.
Input : 11     5              Output : 16'''


def Add(no1, no2):
    return no1 + no2

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Add(no1, no2)

    print("Addition is : ",ret)

if __name__ == "__main__":
    main()
    