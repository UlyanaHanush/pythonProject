# import sqlite3
# import random
# conn = sqlite3.connect('newBaza2 .db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
# n = int(input('число строк: '))
# for i in range(n):
#     a = random.randint(0,9)
#     b = random.randint(0,9)
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?) ''',(a,b))
# cursor.execute(''' SELECT id FROM tab_1''')
# s = cursor.fetchall()
# s1 = random.choice(s)
# cursor.execute(''' SELECT col_1, col_2 FROM tab_1 WHERE id = ?''', s1)
# s2 = cursor.fetchall()
# print(s2)
# if s2[0][0] % 2 == 0 and s2[0][1] % 2 == 0:
#     print('ch')
#     cursor.execute(''' DELETE FROM tab_1 WHERE id = ?''', s1)
# else:
#     print('nech')
#     cursor.execute(''' UPDATE tab_1 SET col_1 = 2, col_2 = 2 WHERE id = ?''', s1)
# cursor.execute(''' SELECT col_1, col_2 FROM tab_1 ''')
# k = cursor.fetchall()
# print(k)
#
# import sqlite3
# conn = sqlite3.connect('newBaza3 .db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INTEGER)''')
# conn.commit()
# cursor.execute(''' SELECT * FROM tab_1 ''')
# s = cursor.fetchall()
# class A:
#     def function(self, a=None, b=None, c=None):
#         if a is not None and b is None and c is None:
#             print('один арг')
#             cursor.execute('''INSERT INTO tab_1(col_1) VALUES (3) ''')
#             conn.commit()
#         elif a is not None and type(b) is int and c is None:
#             print('два арг')
#             cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
#             conn.commit()
#         elif a is not None and b is not None and type(c) is int:
#             print('три арг')
#             (''' UPDATE tab_1 SET col_1 = 77 WHERE id = 3''')
#             conn.commit()
# a = A()
# a.function(2,2)
# #conn.commit()
# cursor.execute(''' SELECT * FROM tab_1 ''')
# s = cursor.fetchall()
#print(s)
#
# import sqlite3
# conn = sqlite3.connect('newBaza4 .db')
# cursor = conn.cursor()
# cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
# for i in range(3):
#     n1 = input('введите данные: ')
#     n2 = input('введите данные: ')
#     cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?,?)''', (n1, n2))
#
#
# #conn.commit()
#
# cursor.execute(''' UPDATE tab_1 SET col_1 = 'hello', col_2 = 'world' WHERE id = 3''')
# cursor.execute('''DELETE FROM tab_1 WHERE id = 2''')
# cursor.execute(''' SELECT * FROM tab_1 ''')
# s = cursor.fetchall()
# print(s)
# with open("newBaza4.txt", "w", encoding='utf-8') as file:
#     for i in s:
#        s1 = ' - '.join([str(i2) for i2 in i])
#        file.write(s1+'\n')
# print(s1)

import sqlite3
conn = sqlite3.connect('newBaza5 .db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, titel TEXT, author TEXT, price INT, amount INT)''')
for i in range(3):
    n1 = input('title: ')
    n2 = input('author: ')
    n3 = input('price: ')
    n4 = input('amount: ')
    cursor.execute('''INSERT INTO tab_1(titel, author, price, amount) VALUES (?,?,?,?)''', (n1, n2, n3, n4))
cursor.execute(''' SELECT * FROM tab_1 ''')
s = cursor.fetchall()
print(s)