'''Write a program which accepts length and width of rectangle and prints area.'''


def area(length, width):
    return length * width

def main():
    length = int(input("Enter length : "))
    width = int(input("Enter width : "))

    Ans = area(length, width)
    print("Area of rectangle is : ",Ans)

if __name__ == "__main__":
    main()