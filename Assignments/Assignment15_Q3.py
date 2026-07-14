'''Write a lambda function using filter() which accepts a list of numbers 
and returns a list of odd numbers.'''

odd = lambda x : x % 2 != 0

def main():
    elements = int(input("Enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    FData = list(filter(odd, arr))

    print(FData)

if __name__ == "__main__":
    main()