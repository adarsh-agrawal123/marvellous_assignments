'''Write a program which accepts one number and 
prints its factors.Input: 12 Output: 1 2 3 4 6 12'''

def factors(no):
    ans = list()
    for i in range(1, no+1):
        if(no % i == 0):
            ans.append(i)

    return ans

def main():
    no = int(input("Enter number : "))
    ret = list(factors(no))
    print(f"factors are : {ret}")

if __name__ == "__main__":
    main()