import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

# Print first 5 cities only
for city in cities[:5]:
    print(city)

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = []
for city in cities:
    temps.append(float(city['temperature']))
print(sum(temps)/len(temps))
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = [float(city['temperature']) for city in cities]
print(sum(temps)/len(temps))
print()
# My code
sum_ger_temp = 0
germany_cities = []
italy_city_temp = []
spain_temp_below_12_cities = []
country = []
max_spain_temp = -float("inf")
for city in cities:
    country.append(city['country'])
    if city['country'] == 'Germany':
        germany_cities.append(city['city'])
        sum_ger_temp += float(city['temperature'])
    elif city['country'] == 'Spain':
        if float(city['temperature']) > 12:
            spain_temp_below_12_cities.append(city['city'])
    elif city['country'] == 'Italy':
        italy_city_temp.append(city['temperature'])
unique_country = set(country)
# Print all cities in Germany
print("All cities in Germany")
for i in germany_cities:
    print(i)
print()


# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
for i in spain_temp_below_12_cities:
    print(i)
print()

# Count the number of unique countries
print("The number of unique countries")
print(len(unique_country))
print()
# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")
print(sum_ger_temp/len(germany_cities))
print()
# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")
print(max(italy_city_temp))
print()