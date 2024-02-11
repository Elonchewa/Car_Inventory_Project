import sqlite3

table1 = '''CREATE TABLE IF NOT EXISTS Inventory (Num INTEGER PRIMARY KEY NOT NULL, 
                                    Car TEXT,
                                    Year INTEGER,
                                    mpg REAL)'''

ini = sqlite3.connect("Inventory.db")
cur= ini.cursor()

cur.execute(table1)

ini.commit()
ini.close()