# 1)
# def a_functoin():
#     print('yes')
# for i in range(4):
#     a_functoin()
#
# a_function()
# 2)
# def a_functoin():
#     pass  # пустая функция
#
#
# a_functoin()
# 3)
# a = 'Hello'
# def a_function():
#     print(a)
#
#
# a_function()
# 4)
# import random
# a = [random.randint(1,9) for i in range(3)]
# print(a)
#
#
# def sum_a():
#     k = 0
#     for i in a:
#         k += i
#     print(f'сумма {k}')
#
#
# sum_a()
# 5)
# import random
#
# a = [random.randint(1, 9) for i in range(3)]
# print(a)
#
#
# def sum_a():
#     k = 0
#     for i in a:
#         k += i
#     return k
#
#
# print(sum_a(), type(sum_a()))
# 6)
# def add(a, b):
#     return a + b
# total = add('hello ', 'world')
# print(total)
# 7)
# def add(a=0, b=0):
#     return a + b
# print(add())
# total = add('hello ', 'world')
# print(total)
# print(add(b=3,a=5))
# 8)
# def add(c, a=0, b=5):
#     return a + b + c
# print(add(1))
# 9)
# def fun(*args, **kwargs): #args = кортеж, kwargs словарь
#     for i in args:
#         print(i)
#     print(kwargs)
#
#
#     fun(1, 2, 'hello', [1, 2, 3], name='uli', job='programmer')
# 10)
# def a_fun():
#     global a
#     a = 1
#     b = 2
#     return a + b
# def b_fun():
#     c = 3
#     return a+c
# print(a_fun())
# print(b_fun())
#11
# a = [1,2,3]
# def a_sum():
#     print(sum(a))
# a_sum()
#12)
# def fun_1 (a,b):
#     def inner_fun(x):
#         return x*x*x
#     return inner_fun(a) + inner_fun(b)
# def a_sum(a,b): return a + b
# # print(a_sum(1,2))
#
# month = int(input('введите номер месяца'))
# def pora(a):
#     if a ==
