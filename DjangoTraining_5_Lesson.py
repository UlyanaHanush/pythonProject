# import sqlite3
# db = sqlite3.connect('uli')
# cursor = db.cursor()
# cursor.execute('''CREATE TABLE custs(id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT unique, password TEXT)''') # создание таблицы
#
# if cursor.execute('''INSERT INTO custs(name, course) VLUES (?,?)''', ('John, Python')):
#     print('record inserted successfully') # вставка записей в таблицу
#
# if cursor.execute('''INSERT INTO custs(name, course) VLUES (:name, :course)''', {'name':'Tom', 'course':'Python'}):
#     print('record inserted successfully')#вставка словаря
#
# if cursor.execute('''INSERT INTO custs(name, course) VLUES (?,?)''', [('Tom', 'Python'), ('Smith', 'Hadoop')]):
#     print('record inserted successfully')#вставка нескольких значений
#
# if cursor.execute('''SELECT name,course FROM custs'''):
#     print('record fetchet successfully')#выборка запесей из таблицы custs автоматически работает как fetchall
# for record in cursor:
#     print('{0},{1}'.format(record[0], record[1]))
#
# if cursor.execute('''SELECT name,course FRON custs WHERE name=?''',('John',)):
#     print('record fetchet successfully')#выборка с именем Джон
# cursor.fetchone()
#
# if cursor.execute('''INSERT INTO custs(name,course) VALUES(?,?)''',('Jonny','R')):
#     print('record fetchet successfully')#получение id
# cursor.lastrowid
#
# if cursor.execute('''UPDATE custs SET course = ? WHERE name = ?''',('Cassandrs','John')):
#     print('record fetchet successfully')#обновление с именем Джон
# db.commit()
# db.rollback() #незафиксированные обновления могут быть откатаны
#
# if cursor.execute('''DELETE FROM custs WHERE name = ?''',('John',)):
#     print('record fetchet successfully')#удаление записи с именем Джон
# db.commit()
# db.rollback()
#
# record1 = cursor.fetchone()#извлечение первой записи
# print(record1)
#
# recordAll = cursor.fetchall()#получение всех записей
# for record in recordAll:
#     print('{0},{1}'.format(record[0], record[1]))
#
# cursor.execute('''DROP TABLE cucts''') # уничтожение таблицы
# db.commit()
# db.close()
##############################
# con.row_factory = lite.Row# подключаем Row
# cur = con.cursor()
# cur.execute("SELECT * FROM Cars")
# rows = cur.fetchone()
# print(rows.keys())#название столбцов
#####################################
# import sqlite3 as lite
# con = lite.connect('test.db')
# with con:
#     cur = con.cursor()
#     cur.execute('''PRAGMA table_info("Cars")''')
#     data = cur.fetchall()
#     for d in data:
#         print(d[0], d[1], d[2])