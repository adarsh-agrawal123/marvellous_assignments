'''Write a program which accepts one number and 
prints multiplication table of that number.Input: 4Output:4 8 12 16 20 24 28 32 36 40'''

def multiplication(no):
    Ans = list()
    for i in range(1,11):
        Ans.append(no*i)

    return Ans

def main():
    no = int(input("Enter number : "))
    Ans = list(multiplication(no))
    print(Ans)

if __name__ == "__main__":
    main()