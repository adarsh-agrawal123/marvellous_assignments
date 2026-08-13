'''Write a program which contains filter(), map() and reduce() in it. 
Python application which contains one list of numbers. List contains the numbers which 
are accepted from user. Filter should filter out all such numbers which are even. 
Map function will calculate its square. Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204'''


from functools import reduce

even = lambda no : (no % 2 == 0)

square = lambda no : no*no

addition = lambda no1, no2 : no1 + no2

def main():
    elements = int(input("Enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        arr.append(int(input()))

    FData = list(filter(even, arr))

    print("List after filter : ",FData)

    MData = list(map(square, FData))

    print("List after map : ",MData)

    RData = reduce(addition, MData)

    print("Output of reduce : ",RData)

if __name__ == "__main__":
    main()