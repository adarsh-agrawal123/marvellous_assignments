'''Write a program which accepts one number and 
prints all odd numbers till that number.Input: 10 Output: 1 3 5 7 9'''


def odd(no):
    ans = list()
    for i in range(1, no+1, 2):
        ans.append(i)

    return ans

def main():
    no = int(input("enter number : "))
    ans = list(odd(no))
    print("result : ",ans)

if __name__ == "__main__":
    main()