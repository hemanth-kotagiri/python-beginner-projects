import sys
import string
import random
import os

class Password:
    def __init__(self):
        try:
            a = list(map(lambda a : True if a == 'y' else False, [input("Include upper-case(y/n): "), input("Include lower-case(y/n): "), input("Include numbers(y/n): "), input("Include symbols(y/n): ")]))
            self.upper = a[0]
            self.lower = a[1]
            self.numeric = a[2]
            self.symbol = a[3]
            self.length = int(input("Enter length of password : "))
        except:
            print("Not a valid input..! ")
            sys.exit(-1)

    def passwordGen(self):
        password = ''
        while len(password) < self.length:
            ls = []
            if self.numeric: ls.append(random.choice(list(string.digits)))
            if self.lower : ls.append(random.choice(list(string.ascii_lowercase)))
            if self.upper : ls.append(random.choice(list(string.ascii_uppercase)))
            if self.symbol : ls.append(random.choice(list(string.punctuation)))
            if not ls: sys.exit(0)
            random.shuffle(ls)
            if self.length - len(password) > len(ls):
                password += ''.join(ls) 
            else:
                password += ''.join(ls[:self.length - len(password)])

        return password

gen = Password()
print(gen.passwordGen())










