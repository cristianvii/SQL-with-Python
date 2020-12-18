SQL - Structured Query Language

Manipulate data in relational database, ( sql server, Access, SQLite, MySQL, Orcale)

Can make "deposits", "withdrawels", and updates 

Consists of Rows, Columns, and Tables


Databases vs Tables

-   Tables contain data for one specific project
-   Columns to show the different features contained
-   Rows to displat the values of each feature at a certain,
    simultaneous measurement

-   databases store many tables, which have extra data describing
    the main attributes of the tables

5 types that data can be stored in
-   Null, Integer, Real, Text(converted to UTF Format), 
    Blob(stored excatly as it was inputted)



#dropping and adding to database

import sqlite3


conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()


c.execute("DROP TABLE iceCubeMelting")


c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT " +
          "PRIMARY KEY,temperature REAL, date TEXT)")


#INSERT INTO tablename VALUES (value1,value2,value3,...)
c.execute("INSERT INTO iceCubeMelting VALUES"+
          " (0,27.0,'28-08-2017') ")
conn.commit()

#INSERT INTO tablename (column1, column2,...,columnN)VALUES
#(?,?,...,?)#(values1,values2,...,valuesN)
for i in range(1,5):
    c.execute("INSERT INTO iceCubeMelting (time,temperature,date)"+
              " VALUES (?,?,?)",(i,27-0.1*i,"28-08-2017"))
conn.commit()
for i in range(5,8):
    c.execute("INSERT INTO iceCubeMelting (time,temperature)"+
              " VALUES (?,?)",(i,27-0.1*i))


for i in range(5,8):
    c.execute("INSERT INTO iceCubeMelting (temperature)"+
              " VALUES (?,?)",(i,27-0.1*i))

    
conn.commit()
c.close()
conn.close

#How to select Data
import sqlite3


conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()


#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT " +
#          "PRIMARY KEY,temperature REAL, date TEXT)")



#SELECT column1,...,columnN FROM tablename
#c.execute("SELECT temperature,time,date FROM iceCubeMelting")


#SELECT * FROM tablename
#c.execute("SELECT * FROM iceCubeMelting")

#SELECT * FROM tablename LIMIT #NoRows OFFSET #Offset
c.execute("SELECT * FROM iceCubeMelting LIMIT 2 OFFSET 1")


#SELECT & FROM tablename ORDER BY cloumn1,column2,...,columnN
#c.execute("SELECT * FROM iceCubeMelting ORDER BY temperature ASC")



#SELECT DISTINCT column1,...,columnN FROM tablename
c.execute("SELECT DISTINCT date,temperature FROM iceCubeMelting")

data = c.fetchall()
for piece in data:
    print(piece)
#print(data
c.close()
conn.close


#CONDITIONAL SEARCHING IN Database
import sqlite3


conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()


#c.execute("CREATE TABLE IF NOT EXISTS iceCubeMelting(time INT " +
#          "PRIMARY KEY,temperature REAL, date TEXT)")



#SELECT column1,...,columnN FROM tablename
#c.execute("SELECT temperature,time,date FROM iceCubeMelting")


#SELECT * FROM tablename
#c.execute("SELECT * FROM iceCubeMelting")

#SELECT * FROM tablename WHERE condition
#>, < =, NOT
#c.execute("SELECT * FROM iceCubeMelting WHERE "+
#          "date = '28-08-2017'")

#c.execute("SELECT * FROM iceCubeMelting WHERE "+
#          "date IS NOT NULL")

#AND or OR
c.execute("SELECT * FROM iceCubeMelting WHERE "+
          "time < 5 OR temperature > 26.2")

data = c.fetchall()
for piece in data:
    print(piece)

c.close()
conn.close


#UPDATING DATA AND DELETING DATA 

import sqlite3


conn = sqlite3.connect("Database/Training.db")
c = conn.cursor()

#UPDATE tablename SET column = values1, ..., columnN = valuesN
#WHERE condition

#c.execute("UPDATE iceCubeMelting SET date = '28-08-2017'"+
#          "WHERE date is NULL")



#c.execute("UPDATE iceCubeMelting SET date = '30-08-2017',"+
#          "temperature = 26.5 WHERE time > 6")


#DELETE FROM tablename WHERE condition
#c.execute("DELETE FROM iceCubeMelting WHERE time < 5")

#DELETE from tablename
c.execute("DELETE FROM iceCubeMelting")


conn.commit()
c.close()
conn.close
