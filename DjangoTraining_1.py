'''
1.Write a program to print the:
a.Number of lowercase “a” and “o” in the following sentence.
b.Number of uppercase “L” and “N” in the following sentence.
‘Discover, Learning, with, Edureka’
'''
# w = 'Discover, Learning, with, Edureka'
# a = 0
# o = 0
# for i in w:
#     if i == 'a':
#         a += 1
#     elif i == 'o':
#         o +=1
#     else:
#         None
# print(f'a: {a}\no: {o}')
'''
2.Write a program to remove the following from:www.edureka.in
a.Remove all w’s before and after .edureka.
b.Remove all lowercase letter before and after .edureka.
c.Remove all printable characters
'''
# e = 'www.edureka.in'
# import re
# s1=re.sub("[edureka]","",e)
# s1=s1.replace("w", "")
# for el in s1:
#     if el.islower():
#         s1=s1.replace(el, "")
# s1=s1.replace("..", ".edureka.")
# for elem in s1:
#     if not el.isalpha():
#         s1 = s1.replace(el, "")
# print(s1)
'''
3.Identify the type of numbers:
a.0X7AE
b.3+4j
c.-01234
d.3.14e-2
'''
# a = 0X7AE
# b = 3+4j
# c = -0o1234
# d = 3.14e-2
#
# y = [a,b,c,d]
# for el in y:
#     if isinstance(el, complex):
#         print('complex')
#     elif isinstance(el, int):
#         print('int')
#     elif isinstance(el, float):
#         print('float')
#     else:
#         print('not a number')
'''
4.Write a program for String Formatting Operator % which should include the following conversions:
a. Character
b. Signed decimal integer
c. Octal integer
d. Hexadecimal integer (UPPERcase letters)
e. Floating point real number
f. Exponential notation (with lowercase 'e')
'''
# try:
#     x = input('str: ')
#     print(type(x))
#     x = float(x)
#     print(int(x))
#     print(hex(int(x)))
#     print(oct(int(x)))
#     print(float(x))
#     print(f'{int(x):.3e}')
# except:
#     print('Not a number')
a = "bay"
b = a[0]
print(type(b))

