'''Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers which are 
accepted from user. Filter should filter out all prime numbers. 
Map function will multiply each number by 2. Reduce will return Maximum number from that 
numbers. (You can also use normal functions instead of lambda functions).
Input List = [2, 70, 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62'''

from functools import reduce

def ChkPrime(no):
    for i in range(2, no):
        if(no % i == 0):
            return False
        
    return True

Multiply = lambda no : no*2

Greater = lambda no1, no2 : no1 if(no1 > no2) else no2

def main():
    elements = int(input("Enter no of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        arr.append(int(input()))
    
    FData = list(filter(ChkPrime, arr))

    print(FData)

    MData = list(map(Multiply, FData))

    print(MData)

    RData = reduce(Greater, MData)

    print(RData)

if __name__ == "__main__":
    main()