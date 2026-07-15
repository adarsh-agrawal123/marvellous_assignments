'''Write a lambda function using filter() which accepts a list of numbers 
and returns a list of numbers divisible by both 3 and 5.'''

divisible = lambda x : x % 3 == 0 and x % 5 == 0

def main():
    elements = int(input("Enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    FData = list(filter(divisible, arr))

    print(FData)

if __name__ == "__main__":
    main()