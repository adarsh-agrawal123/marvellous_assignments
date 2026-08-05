'''Write a program which accept N numbers from user and store it into List. 
Return addition of all elements from that List.
Input : Number of elements : 6 
Input Elements : 13 5 45 7 4 56
Output : 130'''

def add(arr):
    ans = 0
    for no in arr:
        ans = ans + no

    return ans


def main():
    arr = list()
    elements = int(input("Enter number of elements : "))

    print("Input elements : ")

    for i in range(0, elements):
        no = int(input())
        arr.append(no)
    
    ret = add(arr)
    print(f"Sum of elements : {ret}")

if __name__ == "__main__":
    main()
    