import sqlite3

conn = sqlite3.connect('employee.db')

c = conn.cursor()

c.excute("""CREATE TABLE employee (
            first text,
            last text,
            pay integer
        )""")

conn.commit()
conn.close()
