# '''
# 1. Write a program which will find factors of given number and find whether the
# factor is even or odd
# '''
# n = int(input('num: '))
# list = []
# list2 = []
# d = 2
# while d * d <= n:
#     if n % d == 0:
#         n //= d
#         if d % 2 == 0:
#              list.append(d)
#         else:
#             list2.append(d)
#     else:
#         d += 1
# if n > 1:
#     if n % 2 == 0:
#         list.append(n)
#     else:
#         list2.append(n)
#
# print(list)
# print(list2)
# '''
# 2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically.
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
# '''
# list = []
# while True:
#     a = input('???: ')
#     if a == 'stop':
#         break
#     else:
#         list.append(a)
# for i in sorted(list):
#     print(i)
# '''
# 3. Write a program, which will find all the numbers between 1000 and 3000 (both included) such that each digit
# of a number is an even number. The numbers obtained should be printed in a comma separated sequence on a single line.
# Hint: In case of input data being supplied to the question, it should be assumed to  be a console input. Divide each
# digit with 2 and verify is it even or not.
# '''
# list = []
# for i in range(1000,3001):
#     x = ''
#     for j in str(i):
#         if int(j)%2 == 0:
#             x += j
#             if x == str(i):
#                 list.append(i)
# print(list)
# '''
# 4. Write a program that accepts a sentence and calculate the number of letters and
# digits.
# Suppose if the entered string is: Python0325
# Then the output will be:
# LETTERS: 6
# DIGITS:4
# '''
# a = input('??: ')
# LETTERS, DIGITS = 0, 0
# for i in a:
#     if i.isdigit():
#         DIGITS += 1
#     elif i.isalpha():
#         LETTERS += 1
# print(f'LETTERS {LETTERS}\nDIGITS {DIGITS}')
# '''

