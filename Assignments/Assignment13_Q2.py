'''Write a program which accepts radius of circle and prints area of circle.'''

def area(radius):
    return 3.14 * radius * radius

def main():
    radius = int(input("Enter radius : "))
    Ans = area(radius)
    print("Area of circle is : ",Ans)

if __name__ == "__main__":
    main()