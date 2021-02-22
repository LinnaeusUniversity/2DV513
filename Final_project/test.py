# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pymysql

db = pymysql.connect(host='localhost', user='root', password='user1')

cur = db.cursor()

cur.execute("""CREATE SCHEMA IF NOT EXISTS `assignment3`;

""")
cur.execute("""USE `assignment3` ;""")
# cur.execute("""drop SCHEMA IF  EXISTS `assignment3`;""")
db.close()

