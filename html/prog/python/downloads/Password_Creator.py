x = input('I recomend that your password be longer and have signs mixed in.(press enter)')

import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

number = input('Number of passwords? - ')
number = int(number)

length = input('Password length? - ')
length = int(length)

for p in range(number):
    password = ''
    for c in range(length):
        password += random.choice(chars)
    print(password)
#range function is used when you have a list of some sort
#p = password
#c = character
#passwords should be longer and have signs mixed in
