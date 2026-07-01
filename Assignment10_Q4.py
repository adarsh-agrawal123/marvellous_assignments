'''Write a program which accepts one number and 
prints all even numbers till that number.Input: 10 Output: 2 4 6 8 10'''


def EvenSeries(no):
    ans = list()
    for i in range(2,no+1,2):
        ans.append(i)

    return ans

def main():
    no = int(input("enter number : "))
    ans = list(EvenSeries(no))
    print("result : ",ans)


if __name__ == "__main__":
    main()