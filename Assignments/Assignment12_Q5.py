'''Write a program which accepts one number and 
prints that many numbers in reverse order 1.Input: 5 Output: 5 4 3 2 1'''


def main():
    no = int(input("Enter number :"))
    for i in range(no, 0, -1):
        print(i, end=" ")



if __name__ == "__main__":
    main()