import mysql.connector
con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "neeraja123",
    database = "college"
)
cursor = con.cursor()
query = "SELECT name,marks FROM students WHERE marks > %s"
values = (80,)
cursor.execute(query,values)
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
con.close()
