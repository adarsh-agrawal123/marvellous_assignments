'''Write a program which accepts one number and prints cube of that number'''




def cube(No):
    return No*No*No

def main():
    No = int(input("Enter number : "))
    Ans = cube(No)
    print("The cube is : ",Ans)

if __name__ == "__main__":
    main()