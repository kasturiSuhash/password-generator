import random
import string    # string module is to import lower case and upper case strings
def gen_pass(min_len,num=True,spec_char=True):   #num,spec_char is to tell the function to include numbers and special characters
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    characters=letters
    if num:
        characters += digits
    if spec_char:
        characters += special
    passwd = ''
    met_criteria = False
    has_num = False
    has_spec = False
    while not met_criteria or len(passwd)<min_len:
        new_char=random.choice(characters)
        passwd += new_char
        if new_char in digits:
            has_num=True
        elif new_char in special:
            has_spec = True
        met_criteria = True
        if num:
            met_criteria = has_num
        if spec_char:
            met_criteria = met_criteria and has_spec
    return passwd

print("Hey! Welcome to automatic password generator. Please provide the requirements given below.You will get the password in no time!")
print("Ok. Let's get started.")
min_len = int(input("Enter the minimum no.of characters required for the password: "))
has_num = input("Number required in the password (y/n)? ").lower() == "y"
has_spec = input("Special characters required (y/n)? ").lower() == "y"

passwd = gen_pass(min_len,has_num,has_spec)
print("The password is :",passwd)
print("Thank you")
