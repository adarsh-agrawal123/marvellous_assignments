'''Write a lambda function using reduce() which accepts a list of numbers 
and returns the addition of all elements.'''

from functools import reduce

add = lambda no1, no2 : (no1 + no2)

def main():
    elements = int(input("Enter number of elements : "))

    print("Enter elements : ")

    arr = list()

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    result = reduce(add, arr)

    print("Addition of all elements is : ", result)

if __name__ == "__main__":
    main()