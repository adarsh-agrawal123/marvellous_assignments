'''Write a program which accept one number and display below pattern.
Input :       5
Output :      
1
1     2
1     2     3
1     2     3     4
1     2     3     4     5'''


def main():
    no = int(input("Enter number : "))

    for i in range(0, no):
        for j in range(0, i+1):
            print(j+1, end=" ")

        print()

if __name__ == "__main__":
    main()