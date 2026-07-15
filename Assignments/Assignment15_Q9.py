'''Write a lambda function using reduce() which accepts a list of numbers 
and returns the product of all elements.'''

from functools import reduce

mul = lambda no1, no2 : no1*no2

def main():
    elements = int(input("Enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    ret = reduce(mul, arr)

    print(f"Multiplication is : {ret}")

if __name__ == "__main__":
    main()