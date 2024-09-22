#8. Using relational databases
#8.1. Write a program that asks the user to enter the ICAO code of an airport.
# The program fetches and prints out the corresponding airport name and location (town) from the airport database used on this course.
# The ICAO codes are stored in the ident column of the airport table.

import mysql.connector
from geopy.distance import geodesic

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
'''
def get_airport_by_icao_code(icao_code):
    cursor = connection.cursor()
    sql = "select name,municipality from airport where ident = %s"
    cursor.execute(sql,(icao_code.upper(),))
    result = cursor.fetchone()
    return result

def main():
    while True:
        icao_code = input("Enter icao code of the airport: ")
        airport_info = get_airport_by_icao_code(icao_code)
        if airport_info:
            airport_name, municipality = airport_info
            print(f"Airport name: {airport_name}")
            print(f"Location(Town): {municipality}")
        else:
            print(f"No airport found with icao code {icao_code.upper()}")
main()
'''

#8.2. Write a program that asks the user to enter the area code (for example FI) and prints out the
# airports located in that country ordered by airport type. For example, Finland has 65 small airports,
# 15 helicopter airports and so on.
'''
def get_airport_by_country_code(country_code):
    cursor = connection.cursor()
    sql = ("select type,Count(*) as airport_count "
           "from airport "
           "where iso_country = %s "
           "group by type "
           "order by type")
    cursor.execute(sql,(country_code.upper(),))
    result = cursor.fetchall()
    return result

def main():
    while True:
        country_code = input("Enter country code (e.g FI for Finland): ")
        airport_by_type = get_airport_by_country_code(country_code)
        if airport_by_type:
            print(f"Airports in country {country_code}:")
            for airport_type, count in airport_by_type:
                print(f"\t{airport_type}: {count}")
        else:
            print(f"No airport found with country code {country_code.upper()}")
main()
'''
#8.3. Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
# write geopy into the search field and finish the installation.

'''
def get_coordinates_by_icao(icao_code):
    cursor = connection.cursor()
    sql = "select latitude_deg,longitude_deg from airport where ident = %s"
    cursor.execute(sql,(icao_code.upper(),))
    result = cursor.fetchone()
    return result
def calculate_distance(icao1, icao2):
    coords_1 = get_coordinates_by_icao(icao1)
    coords_2 = get_coordinates_by_icao(icao2)
    if coords_1 is None:
        print(f"No airport forund with ICAO code {icao1.upper()}")
    if coords_2 is None:
        print(f"No airport forund with ICAO code {icao2.upper()}")
    distance_km = geodesic(coords_1, coords_2).kilometers
    print(f"The distance between {icao1.upper()} and {icao2.upper()} is {distance_km:.2f} kilometers")

def main():
    while True:
        icao1 = input("Enter icao code of the first airport: ")
        icao2 = input("Enter icao code of the second airport: ")
        calculate_distance(icao1, icao2)
main()

'''