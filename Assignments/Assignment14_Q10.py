'''Write a lambda function which accepts three numbers and returns largest number'''

greater1 = lambda x,y : (x if x>y else y)
greater2 = lambda p,q : (p if p>q else q)

def main():
    no1 = int(input("Enter first number : "))
    no2 = int(input("Enter second number : "))
    no3 = int(input("Enter third number : "))

    ret = greater2(no3, greater1(no1, no2))
    
    print("Largest among three is : ",ret)

if __name__ == "__main__":
    main()