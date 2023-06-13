'''
You have to use fundamentals of Python taught in module 2
1.Read the input from command line –Reference ID
2.Check for validity –it should be 12 digits and allows on number and alphabet
3.Encrypt the Reference ID and print it for reference
'''
import os
import hashlib
import re
while True:
    password = input('input password: ')
    if re.search(r'[A-Za-z\d]{12,12}', password):
            print('OK')
            salt = os.urandom(32)
            key = hashlib.pbkdf2_hmac('sha256', 'password'.encode('utf-8'), salt, 100000)
            break
    else:
            print('Incorrect password. Repeat')
print(f'your password: {password}')

