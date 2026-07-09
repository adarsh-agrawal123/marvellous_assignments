'''Write a program which accepts one number and prints binary equivalent.'''


def binary(no):
    ans = ""
    while no>0:
        bin = no&1
        ans = str(bin) + ans
        no = no >> 1

    return ans


def main():
    no = int(input("Enter number : "))
    ret = binary(no)
    print(f"binary equivalent is : {ret}")


if __name__ == "__main__":
    main()