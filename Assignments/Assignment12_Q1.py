'''Write a program which accepts one character and 
checks whether it is vowel or consonant.Input: a Output: Vowel'''


def chkVowel(char):
    if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' 
       or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' ):
        return "Vowel"
    

def main():
    char = input("Enter a character : ")

    if(chkVowel(char)):
        print("Vowel")
    else:
        print("not a Vowel")


if __name__ == "__main__":
    main()