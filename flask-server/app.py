import mysql.connector
import selenium_getData as sg

# connect mysql
mydb = mysql.connector.connect(
    host="localhost", user="root", password="root", database="seleniumdb")

if (mydb):
    mycursor = mydb.cursor()

    # create database if not exists
    mycursor.execute("CREATE DATABASE IF NOT EXISTS seleniumdb")

    dbresult = []

    # check if table already exists or not
    stmt = "SHOW TABLES LIKE 'PLL'"
    mycursor.execute(stmt)
    result = mycursor.fetchone()

    if result:
        print("Table already exists")

    else:
        print("Table doesn't exist")

else:
    print('not connected')
