'''Write a lambda function using filter() which accepts a list of strings 
and returns a list of strings having length greater than 5.'''

Length = lambda string : len(string) >= 5

def main():
    No_Strings = int(input("Enter number of strings : "))

    arr = list()

    print("Enter strings : ")

    for i in range(0, No_Strings):
        string = input()
        arr.append(string)

    FData = list(filter(Length, arr))

    print(FData)

if __name__ == "__main__":
    main()

