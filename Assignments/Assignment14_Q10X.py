'''Write a lambda function which accepts three numbers and returns largest number'''

greater = lambda x, y, z : x if (x>y and x>z) else (y if y>z else z)

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    no3 = int(input("Enter third number : "))

    print(f"Grater number is : {greater(no1, no2, no3)}")

if __name__ == "__main__":
    main()