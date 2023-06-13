import sqlite3 as lite
import sys
con = lite.connect('test1.db')


with con:
    cur = con.cursor()
    con.row_factory
    cur.execute("SELECT * FROM Cars")


    print(con.row_factory)

#

