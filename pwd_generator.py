import string
import random

def generatePwd(pwdLength, numbers=True, characters=True):
    letters = string.ascii_letters
    digits = string.digits
    specialChars = string.punctuation
    print(letters, digits, specialChars)
    
    usableChars = letters
    if numbers:
        usableChars += digits
    if characters:
        usableChars += specialChars


generatePwd(10)