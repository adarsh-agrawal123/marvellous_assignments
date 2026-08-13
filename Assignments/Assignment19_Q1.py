'''Write a program which contains one lambda function which accepts one parameter and 
return power of two.
Input : 4                      Output : 16
Input : 6                      Output : 64'''


power = lambda no : 2**no

def main():
    no = int(input("Enter number : "))
    ret = power(no)

    print("Output : ",ret)

if __name__ == "__main__":
    main()