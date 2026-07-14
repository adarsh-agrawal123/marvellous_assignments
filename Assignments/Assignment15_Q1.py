'''Write a lambda function using map() which accepts a list of numbers and 
returns a list of squares of each number.'''

square = lambda x : x*x

def main():
    arr = list()
    elements = int(input("enter number of elements : "))

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    MData = list(map(square, arr))

    print(MData)

if __name__ == "__main__":
    main()
