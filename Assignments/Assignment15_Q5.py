'''Write a lambda function using reduce() which accepts a list of numbers 
and returns the maximum element.'''


from functools import reduce


maxi = lambda no1, no2 : no1 if(no1 > no2) else no2

def main():
    elements = int(input("Enter number of elements : "))

    print("Enter elements :")

    arr = list()

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    ret = reduce(maxi, arr)

    print("Max number is : ",ret)

if __name__ == "__main__":
    main()

    