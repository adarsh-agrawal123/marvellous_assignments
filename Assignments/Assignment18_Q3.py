'''Write a program which accept N numbers from user and store it into List. 
Return Minimum number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7 
Output : 5'''

def mini(arr):
    min_element = arr[0]

    for i in range(0, len(arr)):
        if(arr[i] < min_element):
            min_element = arr[i]

    return min_element

def main():
    elements = int(input("enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    ret = mini(arr)

    print("min element is : ",ret)

if __name__ == "__main__":
    main()