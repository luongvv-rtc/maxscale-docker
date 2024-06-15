# CNE 370 Virtualization
# June 2024
# Project: Database Sharding
# Student name: Van Vuong
# Instructor: Christine Sutton


import mysql.connector

# Connect to Database Servers
def db_connection():
    return mysql.connector.connect(
        host="192.168.68.102",
        port="4006",
        user="maxuser",
        password="maxpwd"
    )

# Fetch result from query
def fetch_results(cursor, query):
    cursor.execute(query)
    results = cursor.fetchall()
    output = []
    for result in results:
        if result[0]:
            output.append(result[0])
    return output

# def main
def main():
    db = db_connection()
    cursor = db.cursor()
 # 1. The largest zipcode in zipcodes_one
    print('The largest zipcode in zipcodes_one:')
    query_largest_zipcode = "SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;"
    result_largest_zipcode = fetch_results(cursor, query_largest_zipcode)
    print(result_largest_zipcode[0] if result_largest_zipcode else 'No data found')

#2. All zipcodes where state=KY (Kentucky). You may return just the zipcode column, or all columns.

#3. All zipcodes between 40000 and 41000

#4. The TotalWages column where state=PA (Pennsylvania)

if __name__ == "__main__":
    main()

