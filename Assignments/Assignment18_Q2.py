'''Write a program which accept N numbers from user and store it into List. 
Return Maximum number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34 
Output : 56'''


def maxi(arr):
    max_element = -1

    for i in range(0, len(arr)):
        if(arr[i] > max_element):
            max_element = arr[i]

    return max_element

def main():
    elements = int(input("enter number of elements : "))

    arr = list()

    print("Enter elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)

    ret = maxi(arr)

    print("Max element is : ",ret)

if __name__ == "__main__":
    main()