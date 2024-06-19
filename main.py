# CNE 370 Virtualization
# June 2024
# Project: Database Sharding with Maxscale and MariaDB
# Student name: Van Vuong
# Instructor: Christine Sutton


import mysql.connector
from tabulate import tabulate

# Connect to Database Servers
def db_connection():
    return mysql.connector.connect(
        host="maxscale_container_IP_Address", #Change to the IP Address is listed after this command: "sudo docker inspect maxscale_maxscale_1"
        port="4000",
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

# Split List
def split_list(lst, n):
    result = []
    for i in range(0, len(lst), n):
        result.append(lst[i:i + n])
    return result

# Print out in table format
def print_table(data, title):
    print(title)
    table = tabulate(data, tablefmt='grid')
    print(table)


# def main
def main():
    db = db_connection()
    cursor = db.cursor()
# 1. The largest zipcode in zipcodes_one
    print('------------------------------------------')
    print('| 1. The largest zipcode in zipcodes_one |')
    print('------------------------------------------')
    query_largest_zipcode = "SELECT Zipcode FROM zipcodes_one.zipcodes_one ORDER BY Zipcode DESC LIMIT 1;"
    result_largest_zipcode = fetch_results(cursor, query_largest_zipcode)
    print('The largest zipcode in zipcodes_one: ',result_largest_zipcode[0] if result_largest_zipcode else 'No data found')

#2. All zipcodes where state=KY (Kentucky). You may return just the zipcode column, or all columns.
    print('--------------------------------------------')
    print('| 2. All zipcodes where state=KY (Kentucky)|')
    print('--------------------------------------------')
    query1_zipcodes_KY = "SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE State = 'KY';"
    query2_zipcodes_KY = "SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE State = 'KY';"
    combined_result_zipcodes_KY = fetch_results(cursor, query1_zipcodes_KY) + fetch_results(cursor, query2_zipcodes_KY)
    split_list_zipcode_KY = split_list(combined_result_zipcodes_KY, 12)
    print_table(split_list_zipcode_KY, 'All zipcodes where state = KY')

#3. All zipcodes between 40000 and 41000
    print('-------------------------------------------')
    print('| 3. All zipcodes between 40000 and 41000 |')
    print('-------------------------------------------')
    query_range_zipcodes_one = "SELECT Zipcode FROM zipcodes_one.zipcodes_one WHERE zipcode BETWEEN 40000 AND 41000;"
    query_range_zipcodes_two = "SELECT Zipcode FROM zipcodes_two.zipcodes_two WHERE zipcode BETWEEN 40000 AND 41000;"
    range_zipcodes = fetch_results(cursor, query_range_zipcodes_one) + fetch_results(cursor, query_range_zipcodes_two)
    range_zipcodes_split = split_list(range_zipcodes, 12)
    print_table(range_zipcodes_split, 'All zipcodes between 40000 and 41000')

#4. The TotalWages column where state=PA (Pennsylvania)
    print('---------------------------------------------------------')
    print('| 4. The TotalWages column where state=PA (Pennsylvania) |')
    print('----------------------------------------------------------')
    query1_pa_total_wages = "SELECT TotalWages FROM zipcodes_one.zipcodes_one WHERE state = 'PA';"
    query2_pa_total_wages = "SELECT TotalWages FROM zipcodes_two.zipcodes_two WHERE state = 'PA';"
    pa_total_wages = fetch_results(cursor, query1_pa_total_wages) + fetch_results(cursor, query2_pa_total_wages)
    pa_total_wages_split = split_list(pa_total_wages, 8)
    print_table(pa_total_wages_split, 'The TotalWages column where state = PA')

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()

