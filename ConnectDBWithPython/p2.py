# update 
import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "neeraja123",
    database = "college"
)
cursor = con.cursor()
query = "UPDATE students SET marks = %s WHERE name = %s"
values = (92,"sita")
cursor.execute(query,values)
con.commit()
print("sita marks updated successfully")
print("rows affected:",cursor.rowcount)
cursor.close()
con.close()
