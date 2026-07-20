'''Create on module named as Arithmetic which contains 4 functions as 
Add() for addition, Sub() for subtraction, Mult() for multiplication and Div() for division.
All functions accepts two parameters as number and perform the operation. 
Write on python program which call all the functions from Arithmetic module 
by accepting the parameters from user.'''


from Assignment17_Q1Arithmetic import *

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))

    ret = Add(no1, no2)
    print("Addition is : ",ret)

    ret = Sub(no1, no2)
    print("Subtraction is : ",ret)

    ret = Mul(no1, no2)
    print("Multiplication is : ",ret)

    ret = Div(no1, no2)
    print("Division is : ",ret)

if __name__ == "__main__":
    main()