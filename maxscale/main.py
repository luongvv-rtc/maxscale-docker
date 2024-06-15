# CNE 370 Virtualization
# June 2024
# Project: Database Sharding
# Student name: Van Vuong
# Instructor: Christine Sutton


import mysql.connector
# Connect to Database Servers

def db_connection():
    return mysql.connector.connect(
        host="172.23.0.4",
        port="4000",
        user="maxuser",
        password="maxpwd"
    )

cursor = db.cursor()

# Connect to Zipcodes_One
print('zipcodes_one DB:')
cursor.execute("SELECT Zipcode FROM zipcodes_one.zipcodes_one;")
result = cursor.fetchone()
print(result[0])


# Connect to Zipcodes_Two
print('zipcodes_two DB:')
cursor.execute("SELECT Zipcode FROM zipcodes_two.zipcodes_two;")
result = cursor.fetchone()
print(result[0])

