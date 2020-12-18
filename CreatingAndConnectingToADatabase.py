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
