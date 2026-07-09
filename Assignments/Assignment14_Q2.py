'''Write a lambda function which accepts one number and returns cube of that number.'''

cube = lambda x : x*x*x

def main():
    no = int(input("Enter number : "))
    ret = cube(no)
    print(f"Cube is : {ret}")

if __name__ == "__main__":
    main()