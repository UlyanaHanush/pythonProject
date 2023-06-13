'''
1.What is the output of the following code?
nums =set([1,1,2,3,3,3,4,4])
print(len(nums))
Hint:Set consists unique element
'''
# Answer: 4
'''
2.What will be the output?
d ={"john":40, "peter":45}
print(list(d.keys()))
Hint:d.keys()isthefunctionwhichwillshowkeys.
'''
# Answer: ['john','peter']
'''
3.A website requires a user to input username and password to register.
Write a program to check the validity of password given by user.
Following are the criteria for checking password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Hint: In case of input data being suppliedto the question, it should be assumed to be a console input.
'''
# import re
# username = input('input username: ')
# password = input('input password: ')
# if re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$', password):
#         print('Yes')
# else:
#         print('No')
'''
4.Write a for loop that prints all elements of a list and their position in the list.
a = [4,7,3,2,5,9] 
Hint: Use Loop to iterate through list elements.
'''
# a = [4,7,3,2,5,9]
# count = 0
# for i in a:
#     count +=1
#     print(f'{count} - {i}')
'''
5.Please   write   a   program   which accepts  a   string   from   console   and
print   the characters that have even indexes.
Example: If the following string is given as input to the program: H1e2l3l4o5w6o7r8l9d
Then, the output of the program should be: Helloworld
'''
# a = input('input string: ')
# print(a[::2])
'''
6.Please write a program which accepts a string from console and print it in reverse order.
Example: If the following string is given as input to the program:rise to vote sir
Then, the output of the program should be: ris etov ot esir
'''
# a = input('input string: ')
# print(a[::-1])
'''
7.Please write a program which count and print the numbers of each character in a string input by console.
Example: If the following string is given as input to the program:abcdefgabcThen,
the output of the program should be:a,2c,2b,2e,1d,1g,1f,18.
'''
# a = input('input string: ')
# print(*[(str(a.count(i))+str(i)) for i in a], sep=',')
'''
8.With   two   given   lists   [1,3,6,78,35,55]   and   [12,24,35,24,88,120,155],  
write   a program to make a list whose elements are intersection of the above given lists.
'''
# list1 = [1,3,6,78,35,55]
# list2 = [12,24,35,24,88,120,155]
# print(list(set(list1)&set(list2)))
'''
9.With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing 
all duplicate values with original order reserved.
'''
# list = [12,24,35,24,88,120,155,88,120,155]
# list1 = []
# [list1.append(i) for i in list if i not in list1]
# print(list1)
'''
10.By using list comprehension, please write a program to print the list after removing the value
24 in [12,24,35,24,88,120,155].
'''
# list = [12,24,35,24,88,120,155]
# [list.remove(24) for i in range(list.count(24))]
# print(list)
'''
11.By using list comprehension,
please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
'''
# list1 = [12,24,35,70,88,120,155]
# list2 = list1.copy()
# list1.remove(list2[0])
# list1.remove(list2[4])
# list1.remove(list2[5])
# print(list1)
'''
12.By using list comprehension, please write a program to print the list after removing delete numbers
which are divisible by 5 and 7 in [12,24,35,70,88,120,155].
'''
# list = [12,24,35,70,88,120,155]
# [list.remove(i) for i in list if i%5 == 0 or i%7 == 0]
# print(list)
'''
13.Please  write  a  program  to  randomly  generate  a  list  with  5  numbers, 
which  are divisible by 5 and 7 , between 1 and 1000 inclusive.
'''
# import random
# list = random.sample([i for i in range(1,1000) if i%5 == 0 and i%7 == 0],5)
# print(list)
'''
14.Write  a  program  to  compute  1/2+2/3+3/4+...+n/n+1  with  a  given  n  input  by console (n>0).
Example:If the following n is given as input to the program:5
Then, the output of the program should be:3.55
'''
# n = int(input('input num: '))
# sum=0
# for i in range(1,n+1):
#     sum+=(i/(i+1))
# print(sum)
