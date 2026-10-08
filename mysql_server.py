import mysql.connector

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "mysql_username",
        password = "your password"
        )
    db_cursor = mydb.cursor()
    sql = "CREATE DATABASE IF NOT EXISTS python_accessed_database"
    db_cursor.execute(sql)
    db_cursor.close()
    mydb.close()
    print("python_accessed_database created successfully")

except mysql.connector.Error as Err:
    print("An error occured", Err)