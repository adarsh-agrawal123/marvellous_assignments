'''Write a program which accepts two numbers and 
prints addition, subtraction, multiplication and division.'''

def calculation(no1, no2):
    ans = list()

    ans.append(no1 + no2)

    ans.append(no1 - no2)

    ans.append(no1 * no2)

    ans.append(no1 / no2)

    return ans


def main():
    print("Enter two numbers : ")
    no1 = int(input("no1 : "))
    no2 = int(input("no2 : "))

    ans = list(calculation(no1, no2))

    print("addition is : ",ans[0])
    print("subtraction is : ",ans[1])
    print("multiplication is : ",ans[2])
    print("division is : ",ans[3])

if __name__ == "__main__":
    main()