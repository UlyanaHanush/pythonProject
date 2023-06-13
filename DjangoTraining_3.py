'''1.Build an interactive application which should simulate a Quiz contest.
The following questions might be asked as input from user:
Choose level (easy, intermediate, and hard):
3 modes of difficulty and user should input one of these choices.

Please give us the number of question you want to attempt:
No of questions thrown should be the number entered through this prompt.

Specify the question type (multiplication:M, addition:A, subtraction:S, division:D):
One of these operations to be performed.

If the answer is right or wrong, appropriate messages should be printed and move to next question
if attempt count is not exceeded.

Hint:Random utility can be used to change complexity of questions.

The program should ask if the user wants to continue even after attempting
the number of questions specified and accordingly should loop or terminate.
'''
# import random
#
# print('level\n'
#       '1 - easy\n'
#       '2 - intermediate\n'
#       '3 - hard')
# level = input('Choose level: ')
# num_que = int(input('Please give us the number of question you want to attempt: '))
# specify_que = input('Specify the question type (multiplication:M, addition:A, subtraction:S, division:D): ')
#
#
# def question(num1,num2):
#     if specify_que == 'M':
#         print(f'{num1}*{num2}=?')
#         resultat = num1 * num2
#         for el in range(num_que):
#             ans = input('Your answer: ')
#             try:
#                 if int(ans) == resultat:
#                     print('You are right')
#                 else:
#                     print(f'No. You are not right')
#             except:
#                 print('not correct answer')
#         print(f'correct answer {resultat}')
#     elif specify_que == 'A':
#         print(f'{num1}+{num2}=?')
#         resultat = num1 + num2
#         for el in range(num_que):
#             ans = input('Your answer: ')
#             try:
#                 if int(ans) == resultat:
#                     print('You are right')
#                 else:
#                     print(f'No. You are not right')
#             except:
#                 print('not correct answer')
#         print(f'correct answer {resultat}')
#     elif specify_que == 'S':
#         print(f'{num1}-{num2}=?')
#         resultat = num1 - num2
#         for el in range(num_que):
#             ans = input('Your answer: ')
#             try:
#                 if int(ans) == resultat:
#                     print('You are right')
#                 else:
#                     print(f'No. You are not right')
#             except:
#                 print('not correct answer')
#         print(f'correct answer {resultat}')
#     elif specify_que == 'D':
#         print(f'{num1}/{num2}=?')
#         resultat = num1 / num2
#         for el in range(num_que):
#             ans = input('Your answer: ')
#             try:
#                 if int(ans) == resultat:
#                     print('You are right')
#                 else:
#                     print(f'No. You are not right')
#             except:
#                 print('not correct answer')
#         print(f'correct answer {resultat}')
#
#
# def level_que(level):
#     if level=='1' or level=='easy':
#         num1 = random.randint(1,10)
#         num2 = random.randint(1, 10)
#         question(num1,num2)
#     elif level=='2' or level=='intermediate':
#         num1 = random.randint(1, 100)
#         num2 = random.randint(1, 100)
#         question(num1,num2)
#     elif level=='3' or level=='hard':
#         num1 = random.randint(1, 1000)
#         num2 = random.randint(1, 1000)
#         question(num1,num2)
#
#
# level_que(level)
'''
2.Write a recursive function to compute x raised to the power of n.
'''
# def power(num, exp):
#     if (exp == 1):
#         return (num)
#     else:
#         return (num * power(num, exp - 1))
# num = int(input('input number: '))
# exp = int(input('input exponentiation: '))
# print(f'The result of exponentiation is: {power(num, exp)}')
'''
3.Sort the list using lambda function mylist = [["john", 1, "a"], ["larry", 0, "b"]]. 
Sort the list by second item 1 and 0.
'''
# mylist = [["john", 1, "a"], ["larry", 0, "b"]]
# sorted_list1 = sorted(mylist, key=lambda x: x[1])
# sorted_list0 = sorted(mylist, key=lambda x: x[0])
# print(f'{sorted_list1}\n{sorted_list0}')
'''
4.Sort the list using operator.itemgetter function mylist = [["john", 1, "a"], ["larry", 0, "b"]].
Sort the list by second item 1 and 0.
'''
# mylist = [["john", 1, "a"], ["larry", 0, "b"]]
# from operator import itemgetter
# sorted_0 = sorted(mylist, key=itemgetter(0))
# sorted_1 = sorted(mylist, key=itemgetter(1))
# print(f'{sorted_1}\n{sorted_0}')