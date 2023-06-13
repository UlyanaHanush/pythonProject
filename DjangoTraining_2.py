'''
1.Correct theprogram given below.
'''
# total = input('What is the total amount for your online shopping? ')
# country = input('Shipping within the US or Canada? ')
# if country == "US":
#     if total <= "50":
#         print("Shipping Costs $6.00")
#     elif total <= "100":
#         print("Shipping Costs $9.00")
#     elif total <= "150":
#         print("Shipping Costs $12.00")
#     else:
#         print("FREE")
# elif country == "Canada":
#     if total <= "50":
#         print("Shipping Costs $8.00")
#     elif total <= "100":
#         print("Shipping Costs $12.00")
#     elif total <= "150":
#         print("Shipping Costs $15.00")
#     else:
#         print("FREE")
# else:
#     print('no information')
'''
2.Write a program that usesraw_inputto prompt a user for their nameand then welcomes them.
Example: Enter your name: Chuck Hello Chuck
'''
# name = input('Enter your name: ')
# print(f'Hello, {name}')
'''
3.Write a program which prompts the user for a Fahrenheittemperature,
convert the temperature to Celsius and print out the converted temperature.
'''
# temp = int(input('enter Fahrenheittemperature: '))
# print((temp-32)*5/9)
'''
4.Write a program to prompt the user for hours and rate per hour to compute gross pay.
Example:
Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25
'''
# Hours = int(input('Enter Hours: '))
# Rate = float(input('Enter Rate: '))
# print(f'Pay {Hours*Rate}')
'''
5.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9]
'''
# a = [4,7,3,2,5,9]
# for el in a:
#     print(f'{a.index(el)+1} -- {el}')
'''
6.Write a program which should create a dictionary of key:
values.'A':1 'B':2 'C':3 . . . . 'Z':26 [Use dictionary comprehension]
'''
# import string
# val = string.ascii_uppercase
# d = {key: (i+1) for i, key in enumerate(val)}
# print(d)
'''
7.Write a program to reverse/inverse key:
value like below.dict1 = { 'a': 1, 'b':2 }
Expected result :dict2 = { 1: 'a', 2: 'b' }
'''
# dict1 = { 'a': 1, 'b':2 }
# dict = {}
# for val,key in dict1.items():
#     dict[key]=val
# print(dict)
'''
8.Using given list L = ['a', 'b', 'c', 'd'] create a dictionary of key:values.
Expected result {'a': 1, 'c': 3, 'b': 2, 'd': 4}[Hint: Use Enumerate function]
'''
# L = ['a', 'b', 'c', 'd']
# d = {key: (i+1) for i, key in enumerate(L)}
# print(d)
'''
9.Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range print an error.
If the score is between 0.0 and 1.0, print a grade using the following table:
Score     Grade
>= 0.9  A
>= 0.8  B
>= 0.7  C
>= 0.6  D
< 0.6   FAIL
Sample Output:
Enter score: 0.95A
Enter score: 11.5
Bad score
Enter score: 10.0
Bad score
Enter score: 0.75C
Enter score: 0.5FAIL
'''
# prompt = float(input('to prompt for a score between 0.0 and 1.0: '))
# if 0.0 <= prompt <= 1.0:
#     if prompt >= 0.9:
#         print('A')
#     elif prompt >= 0.8:
#         print('B')
#     elif prompt >= 0.7:
#         print('C')
#     elif prompt >= 0.6:
#         print('D')
#     elif prompt < 0.6:
#         print('FAIL')
# else:
#     print('Bad score')