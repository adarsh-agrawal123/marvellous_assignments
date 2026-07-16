'''Write a program which display first 10 even numbers on screen.
Output :      2     4     6     8     10    12    14    16    18    20'''


def main():
    i = 0
    no = 1
    while(i < 10):
        if(no % 2 == 0):
            print(no, end=" ")
            i = i+1

        no = no + 1

if __name__ == "__main__":
    main()
        