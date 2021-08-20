import sqlite3

  #define a connetction

  connection = sqlite3.connect('store_transactions.db')

  cursor = connection.cursor()

  #create store table

  command1 = """CREATE TABLE IF NOT EXISTS
  stores(store_id INTEGER PRIMARY KEY, location TEXT)"""

  cursor.execute(cammand1)