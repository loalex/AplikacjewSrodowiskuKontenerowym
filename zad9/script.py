import mysql.connector
import os

db_host = os.getenv("MYSQL_HOST", "db")
db_user = os.getenv("MYSQL_USER", "user")
db_password = os.getenv("MYSQL_PASSWORD", "password")
db_database = os.getenv("MYSQL_DATABASE", "my_database")

# Łączenie z bazą danych
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_database
)

cursor = connection.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor.fetchall():
    print(table)

cursor.close()
connection.close()
