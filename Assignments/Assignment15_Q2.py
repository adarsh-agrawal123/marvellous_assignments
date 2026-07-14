'''Write a lambda function using filter() which accepts a list of numbers 
and returns a list of even numbers.'''

chkEven = lambda x : (x % 2 == 0)

def main():
    arr = list()
    elements = int(input("Enter number of elements : "))
    print("Input elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    even = list(filter(chkEven, arr))

    print(even)
    

if __name__ == "__main__":
    main()