# Install Mysql on you computer
# https://dev.mysql.com.downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import pymysql


try:
    # Connect to MySQL server
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='mypass'  # Update this with your MySQL password
    )
    print("Connected to MySQL server!")

     # Create a cursor object
    cursor = connection.cursor()

    # Define the database name
    database_name = "elderco"

    # SQL query to create a database
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")
    print(f"Database '{database_name}' created successfully!")

except pymysql.MySQLError as err:
    print(f"Error: {err}")
finally:
    # Close the connection
    if 'connection' in locals():
        cursor.close()
        connection.close()
        print("Connection closed.")
