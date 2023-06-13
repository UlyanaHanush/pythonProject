def fun(x):
    if type(x) is tuple:
        print(f'функция кортеж {sum([len(str(el)) for el in x])}')
    elif type(x) is list:
        print(f'функция list элемент int {sum([len(str(el)) for el in x if type(el) is int])}')
        print(f'функция list элемент str {sum([len(str(el)) for el in x if type(el) is str])}')
    elif type(x) is int:
        print(f'функция int {len([el for el in str(x) if int(el)%2!=0])}')
    elif type(x) is str:
        print(f'функция str {len(x)}')
fun('mama')
fun(13457)
fun((1, 3, 'mamma'))
fun(['mamamama', 1, 222, 45])