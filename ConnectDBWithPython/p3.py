# Delete
import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "neeraja123",
    database = "college"
)
cursor = con.cursor()
query = "DELETE FROM students WHERE marks < %s"
values = (80,)
cursor.execute(query,values)
con.commit()
print("low marks students selected")
print("rows affected:",cursor.rowcount)
cursor.close()
con.close()
