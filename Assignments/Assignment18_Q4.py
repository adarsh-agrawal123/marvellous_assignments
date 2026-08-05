'''Write a program which accept N numbers from user and store it into List. 
Accept one another number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3'''


def counting(arr, search):
    count = 0

    for i in range(0, len(arr)):
        if(arr[i] == search):
            count = count + 1

    return count


def main():
    arr = list()
    elements = int(input("Enter number of elements : "))

    print("Input elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    search = int(input("Enter element to search : "))

    countElement = counting(arr, search)
    print(f"Frequency is : {countElement}")


if __name__ == "__main__":
    main()
