import sqlite3
conn = sqlite3.connect('movie .db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS movie(movie_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, release_year INTEGER, genre TEXT)''')

def add_movie():
    n1 = input('name: ')
    n2 = input('release_year: ')
    n3 = input('genre: ')
    cursor.execute('''INSERT INTO movie(name, release_year, genre) VALUES (?,?,?)''', (n1, n2, n3))
    conn.commit()
def info_movie():
    cursor.execute(''' SELECT * FROM movie ''')
    s1 = cursor.fetchall()
    print(s1)
def info_one_movie():
    n = input('ведите номер фильма: ')
    cursor.execute(''' SELECT name, release_year, genre FROM movie WHERE movie_id = ?''', n)
    s2 = cursor.fetchall()
    print(s2)
while True:
    n = int(input('введите дествие:\n'
          '1 - add_movie\n'
          '2 - info_movie\n'
          '3 -  info_one_movie\n'
          '0 - выход\n'
                  '... '))
    if n == 1:
        add_movie()
    elif n == 2:
        info_movie()
    elif n == 3:
        info_one_movie()
    elif n==0:
        break





