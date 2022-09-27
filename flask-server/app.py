import mysql.connector
import selenium_getData as sg


def db():
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
            mycursor.execute("SELECT lan,lvl,avg_per_func FROM PLL")

            for i in mycursor:
                dbresult.append(i)

            mycursor.close()
            mydb.close()
        else:
            # get table data using selenium
            data = sg.webDriver()

            # create headers of the table
            headers = []
            for i in data[0]:
                headers.append(i)

            # create table if not exists
            mycursor.execute(
                "CREATE TABLE IF NOT EXISTS PLL (lan VARCHAR(100), lvl VARCHAR(100),avg_per_func VARCHAR(100), id int PRIMARY KEY AUTO_INCREMENT)")

            # insert data in the DB
            for dt in data:
                mycursor.execute(
                    "INSERT INTO PLL (lan, lvl, avg_per_func) VALUES (%s, %s, %s)", (dt[headers[0]], dt[headers[1]], dt[headers[2]]))
                mydb.commit()

            # select all data of the table
            mycursor.execute("SELECT lan,lvl,avg_per_func FROM PLL")

            for i in mycursor:
                dbresult.append(i)

            mycursor.close()
            mydb.close()

        return dbresult

    else:
        return "Connection Error"


print(db())
