import sqlite3
#создать БД
conn = sqlite3.connect('name.db')
#обьект курсор для взаимодествия с БД
cursor = conn.cursor()
#таблица с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT)''')
#заполняем таблицу
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES ('hello', 'world') ''')

d = 'red'
f = 'black'
cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?) ''',(d,f)) # переменные в кортежеб если переменная одна не забыть запятую
#conn.commit()
#cursor.execute(''' SELECT * FROM tab_1 WHERE col_1 = 'hello' ''') # для получения первого реультата
#cursor.execute(''' SELECT * FROM tab_1 ORDER BY col_3''') #сортирует все относительно col_3
#cursor.execute(''' SELECT * FROM tab_1 WHERE col_3 LIKE '7%' ''') #З
t=3
cursor.execute('''UPDATE tab_1 SET col_1='world' WHERE id=?''', (t,))
cursor.execute(''' SELECT * FROM tab_1''')
k = cursor.fetchall()
print(k)