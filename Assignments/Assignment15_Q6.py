'''Write a lambda function using reduce() which accepts a list of numbers 
and returns the minimum element.'''


from functools import reduce

mini = lambda no1, no2 : no1 if(no1 < no2) else no2

def main():
    elements = int(input("Enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    ret = reduce(mini, arr)

    print(f"Minimum number is : {ret}")

if __name__ == "__main__":
    main()