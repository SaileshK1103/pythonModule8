#8. Using relational databases
#8.1. Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

import mysql.connector

connection = mysql.connector.connect(
    user = 'sailesh',
    password = 'sailesh1103',
    host = 'localhost',
    port = '3306',
    database = 'flight_game',
    autocommit = True,
    charset = 'utf8mb4',
    collation = 'utf8mb4_unicode_ci'
)
def fetch_airports(icao_code):
    cursor = connection.cursor()
    sql = "select ident,name,municipality from airport where ident = %s"
    cursor.execute(sql,(icao_code,))
    return cursor.fetchone()
def main():
    while True:
        icao_code = input("Enter icao code of the airport: ").upper()
        if icao_code=="":
            print("Invalid entry, please try again.")
            break
        else:
            result = fetch_airports(icao_code)
            print(f"The IATA code {result[0]} with airport name {result[1]} and location town is {result[2]}.")

main()