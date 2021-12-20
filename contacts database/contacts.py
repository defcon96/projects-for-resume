import sqlite3

  #define a connetction

  connection = sqlite3.connect('store_transactions.db')

  cursor = connection.cursor()

  #create store table

  

  cursor.execute(cammand1)
