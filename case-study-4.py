'''
1.A Robot moves in a Plane starting from the origin point (0,0). The robot can move toward UP, DOWN, LEFT, RIGHT.
The trace of Robot movement is as given following:
UP 5
DOWN 3
LEFT 3
RIGHT 2
The numbers after directions are steps.
Write a program to compute the distance current position after sequence of movements.
Hint: Use math module.
'''
# import math
# x = 3-2
# y = 5-3
#
# def distance (x=0, y=0):
#     return math.sqrt(x**2+y**2)
# print(distance(x,y))
'''
2.Data of XYZ company is stored in sorted list.
Write a program for searching specific data from that list.
Hint: Use if/elif to deal with conditions.
'''
# list = ['X', 'Y', 'Z']
# list = sorted(list)
# for i in list:
#     if i == 'X':
#         print('It is X')
#     elif i == 'Y':
#         print('It is Y')
#     elif i == 'Z':
#         print('It us Z')
'''
3.Weather forecasting organization wants to show is it day or night.
So, write a program for such organization to findwhether is it dark outside or not.
Hint: Use time module.
'''
# import time
# struct = time.localtime()
# if 7<struct.tm_hour<23:
#     print('day')
# else:
#     print('night')
'''
4.Write a program to find distance between two locations when their latitude and longitudes are given.
Hint: Use math module.
'''
# import math
# def distance_point (lat1, lon1, lat2, lon2):
#     print(math.sqrt((lat1-lat2)**2 + (lon1-lon2)**2))
#
# lat1 = int(input('input latitude 1: '))
# lon1 = int(input('input longitudes 1: '))
# lat2 = int(input('input latitude 2: '))
# lon2 = int(input('input longitudes 2: '))
# distance_point(lat1, lon1, lat2, lon2)
'''
5.Design a software for bank system. There should be options like cash withdraw, cash credit and change password.
According to user input, the software should provide required output.
Hint: Use if else statements and functions.
'''
# print('1 - cash withdraw\n'
#       '2 - cash credit\n'
#       '3 - change password')
# many = 0
# while True:
#     try:
#         operation = int(input('change: '))
#         if operation == 1 and many >0:
#             amount = int(input('amount of cash: '))
#             many-= amount
#             print(f'cash {amount} withdraw')
#         elif operation == 1 and many == 0:
#             print('no many')
#         elif operation == 2:
#             amount = int(input('amount of cash: '))
#             many  += amount
#             print(f'cash {amount} credit')
#         elif operation == 3:
#             password = input('new password: ')
#             cash-= amount
#             print(f'new password {password}')
#         else:
#             print('incorrect input')
#     except ValueError:
#         print('it is not int')
'''
6.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in acomma-separated sequence on a single line.
'''
# program =[i for i in range(2000,3201) if i%7 == 0 and i%5 !=0]
# print(program)
'''
7.Write a program which can compute the factorial of a given numbers.
Use recursion to find it.
Hint: Suppose the following input is supplied to the program:8.Then, the output should be:40320
'''
# def factorial_recursive(n):
#     if n == 1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
# print(factorial_recursive(int(input('num: '))))
'''
8.Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H: C is 50. H is 30.
D  is  the  variable  whose  values  should  be  input  to  your  program  in  a  comma-separated sequence.
Example:
Let  us  assume  the  following  comma  separated  input  sequence  is  given  to  the program:
100,150,180
The output of the program should be:18,22,24
'''
# import math
# C=50
# H=30
# def program(*D):
#     for i in D:
#         print(f'{math.sqrt(2 *C* int(i)/H):.0f}')
# program(100,150,180)
'''
9.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
The element value in the i-th row and j-th column of the array should be i*j.Note:
i=0,1.., X-1; j=0,1,¡-Y-1.
Example:Suppose the following inputs are given to the program:3,5
Then, the output of the program should be:[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
# X = int(input('Num X: '))
# Y = int(input('Num Y: '))
# list = [[i*ii for i in range(Y)] for ii in range(X)]
# print(list)
'''
10.Write a program that accepts a comma separated sequence of words as input and prints the words
in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:without,hello,bag,world
Then, the output should be:bag,hello,without,world
'''
# words = input('input words: ')
# print(','.join(sorted(words.split(','))))
'''
11.Write a program that accepts sequence of lines as input and prints the lines after making
all characters in the sentence capitalized. Suppose the following inputis supplied to the program:
Hello worldPractice makes perfectThen, the output should be:HELLO WORLDPRACTICE MAKES PERFECT
'''
# sequence = input('input sequence: ')
# print(sequence.upper())
'''
12.Write a program that accepts a sequence of whitespace separated words as input and  
prints   the   words   after   removing   all   duplicate   words   and   sorting   them alphanumerically.
Suppose the following input is supplied to the program:hello world and practice makes perfect
and hello world again
Then, the output should be:again and hello makes perfect practice world
'''
# sequence = input('input a sequence of whitespace separated words: ')
# print(' '.join(sorted(list(set(sequence.split(' '))))))
'''
13.Write  a  program  which  accepts  a  sequence  of  comma  separated  4  digit  binary numbers 
as  its  input  and  then  check  whether  they  are  divisible  by  5  or  not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:0100,0011,1010,1001Then the output should be:1010
'''
# num = input('input bin num: ')
# print([i for i in num.split(',') if int(i,2)%5==0])
'''
14.Write  a  program  that  accepts  a  sentence  and  calculate  the  number 
of  upper  case letters and lower case letters.Suppose the following
input is supplied to the program:Hello world!Then, the output should be:
UPPER CASE 1LOWER CASE 9
'''
# sentence = input('input sentense: ')
# print(f'LOWER: {len([i for i in sentence if i.islower()])}')
# print(f'UPPER: {len([i for i in sentence if i.isupper()])}')
'''
15.Give example of fsum and sum function of math library.
'''
# import math
# print(math.fsum([1, 2, 3, 4, 5]))
# print(sum([1, 2, 3, 4, 5]))
#
# print(math.fsum([100, 400, 340, 500]))
# print(sum([100, 400, 340, 500]))
#
# print(math.fsum([1.7, 0.3, 1.5, 4.5]))
# print(sum([1.7, 0.3, 1.5, 4.5]))