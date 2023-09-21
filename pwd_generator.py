import string
import random

def generate_pwd(min_length, numbers=True, characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    
    usable_chars = letters
    if numbers:
        usable_chars += digits
    if characters:
        usable_chars += special_chars

    pwd = ""
    meets_requirements = False
    has_numbers = False
    has_special_chars = False

    while not meets_requirements or len(pwd) < min_length:
        new_character = random.choice(usable_chars)
        pwd += new_character

        if new_character in digits:
            has_numbers = True
        if new_character in special_chars:
            has_special_chars = True

        meets_requirements = True
        if numbers:
            meets_requirements = has_numbers
        if characters:
            meets_requirements = has_special_chars
        if numbers and characters:
            meets_requirements = has_numbers and has_special_chars

    return pwd        


print("\nSo you need a password, huh?\n")
min_length = int(input("How many characters do you need, minimum? "))
numbers = input("And would you like some numbers with that? (y/n) ").lower() == 'y'
characters = input("And a few special characters? (y/n) ").lower() == 'y'
pwd = generate_pwd(min_length, numbers, characters)
print("\nYour password, should you choose to accept it:", pwd)