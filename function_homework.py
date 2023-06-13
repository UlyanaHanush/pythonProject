while True:
    try:
        n = input('выбор действия + * / -: или 0 для завершения: ')
        def calk_plus(a,b): return a+b
        def calk_minus(a,b): return a-b
        def calk_del(a,b): return a/b
        def calk_umn(a,b): return a*b
        if n=='+':
            print(calk_plus(int(input('число 1: ')), int(input('число 2: '))))
        elif n=='*':
            print(calk_umn(int(input('число 1: ')), int(input('число 2: '))))
        elif n=='-':
            print(calk_minus(int(input('число 1: ')), int(input('число 2: '))))
        elif n=='/':
            print(calk_del(int(input('число 1: ')), int(input('число 2: '))))
        elif n=='0':
            break
    except ZeroDivisionError:
        print('деление на ноль')