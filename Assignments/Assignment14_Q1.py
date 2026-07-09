'''Write a lambda function which accepts one number and returns square of that number.'''

square = lambda x : x*x

def main():
    no = int(input("Enter number : "))
    ret = square(no)
    print(f"square is : {ret}")

if __name__ == "__main__":
    main()