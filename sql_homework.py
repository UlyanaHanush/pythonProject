import sqlite3
import random
conn = sqlite3.connect('newBaza.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT)''')
n = int(input('число строк: '))
for i in range(n):
    a = random.randint(0,9)
    b = random.randint(0,9)
    cursor.execute('''INSERT INTO tab_1(col_1, col_2) VALUES (?, ?) ''',(a,b))
cursor.execute(''' SELECT col_1, col_2 FROM tab_1 ''')
k = cursor.fetchall()
print(k)
list = []
for el in k:
    for el_2 in el:
        list.append(el_2)
sr_arifm = sum(list)/(2*n)
print(sr_arifm)
if sr_arifm > len(K):
    cursor.execute('''DELETE FROM tab_1 WHERE id = 4''')
print(k)

