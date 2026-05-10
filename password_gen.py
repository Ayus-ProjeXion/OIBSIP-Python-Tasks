#project:random password generator
#name:Ayusman Mishra
import random
import string
def main():
    print("Password Generator by Ayusman")
    length=int(input("Enter the desired password length: "))
    letters=string.ascii_letters
    numbers=string.digits
    symbols=string.punctuation
    all_characters=letters+numbers+symbols
    password="".join(random.choice(all_characters)for i in range(length))
    print(f"Your generated password is: {password}")
if __name__=="__main__":
    main()
