'''Write a lambda function using filter() which accepts a list of numbers 
and returns the count of even numbers.'''


even = lambda x : (x % 2 == 0)

def main():
    elements = int(input("Enter number of elements : "))

    print("Enter elements : ")

    arr = list()

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    count = len(list(filter(even, arr)))

    print(f"Total number of even elements : {count}")

if __name__ == "__main__":
    main()