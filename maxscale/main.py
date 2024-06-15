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

# Fetch result
def fetch_results(cursor, query):
    cursor.execute(query)
    return [result[0] for result in cursor.fetchall() if result[0] != ""]

# def main
def main():
    db = db_connection()
    cursor = db.cursor()




if __name__ == "__main__":
    main()

