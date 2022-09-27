import mysql.connector

# connect mysql
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="seleniumdb")

if (mydb):
    print("connected")

else:
    print('not connected')
