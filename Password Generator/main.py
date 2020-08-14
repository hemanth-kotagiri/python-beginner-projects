import sys
import string
import random
import os

def passwordGen(n):
    """ Takes in the parameter n strictly greater than  7 representing the number of characters"""
    
    if n<7:
        print("Password length must be greater than or equal to 7")
        sys.exit(0)
    
    password = ''
    while len(password) < n:
        digit = random.choice(list(string.digits))
        lwr = random.choice(list(string.ascii_lowercase))
        upr = random.choice(list(string.ascii_uppercase))
        punc = random.choice(list(string.punctuation))
        ls = [digit, lwr, upr, punc]
        random.shuffle(ls)
        if n - len(password) > 4:
            password += ''.join(ls) 
        else:
            password += ''.join(ls[:n - len(password)])


    return password

print(passwordGen(15))






