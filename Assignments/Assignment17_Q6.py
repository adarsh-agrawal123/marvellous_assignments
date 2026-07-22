'''Write a program which accept one number and display below pattern.
Input :       5
Output :      
*     *     *     *     *
*     *     *     *
*     *     *
*     *
*   '''


def main():
    no = int(input("Enter number : "))

    for i in range(0, no):
        print("*"*(no-i))

if __name__ == "__main__":
    main()