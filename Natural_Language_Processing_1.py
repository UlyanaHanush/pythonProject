'''
1.Write a program which will find factors of given number and find whether the factor is even or odd.
Hint: Use Loop with if-else statements
'''
# def primfacs(n):
#    i = 2
#    primfac = []
#    while i * i <= n:
#        while n % i == 0:
#            primfac.append(i)
#            n = n / i
#        i = i + 1
#    if n > 1:
#        primfac.append(n)
#    print(primfac)
# num = primfacs(int(input('input num: ')))
'''
2.Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them
alphabetically.
Hint: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
# word = input('input: ')
# list = word.split()
# print(sorted(list))
'''
3.Write a program, whichwill find all the numbers between 1000 and 3000 (both included) such that each digit of a number
is an even number.
The numbers obtained should be printed in a comma separated sequence on a single line.Hint: In case of input data
being supplied to the question,
it should be assumed to be a console input.Divide each digit with 2 and verify is it even or not.
'''
# list = []
# for i in range(1000, 3001):
#     if i %2 ==0:
#         list.append(i)
# print(list)
'''
4.Write a program that accepts a sentence and calculate the number of letters and digits.Suppose if the entered string is:
Python0325Then the output will be:LETTERS: 6DIGITS:4Hint: Use built-in functions of string.
'''
# LETTERS = 0
# DIGITS = 0
# w = input('input: ')
# for i in w:
#     if i.isalpha():
#         LETTERS +=1
#     elif i.isdigit():
#         DIGITS +=1
#     else:
#         None
# print(f'LETTERS: {LETTERS}\nDIGITS: {DIGITS}')
'''
5.Design a code which will find the given number is Palindrome number or not.
Hint: Use built-in functions of strin0
'''
# num = input('input num: ')
# if num.isdigit():
#     if num[:] == num[::-1]:
#         print('is Palindrome')
#     else:
#         print("isn't Palindrome")
# else:
#     print("isn't DIGITS")