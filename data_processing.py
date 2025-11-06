import csv, os
def filter(condition, dict_list:dict) -> dict:
    dict_return = []
    for item in dict_list:
        if condition(item):
            dict_return.append(item)
    return dict_return
        
        
def aggregate(aggregation_key, aggregation_function, dict_list):
    temps = []
    for item in dict_list:
        try:
            temps.append(float(item[aggregation_key]))
        except ValueError:
            temps.append(item[aggregation_key])
    return aggregation_function(temps)


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
print()

# Print the average temperature of all the cities
print("The average temperature of all the cities:")
temps = aggregate('temperature',lambda x:sum(x)/len(x), cities)
print(temps)
print()

# My code
# Print all cities in Germany
print("All cities in Germany")
filter_germany = filter(lambda x:x['country'] == 'Germany', cities)
for i in filter_germany:
    print(i)
print()


# Print all cities in Spain with a temperature above 12°C
print("All cities in Spain with a temperature above 12°C")
filter_temp_spain = filter(lambda x:x['country'] == 'Spain' and float(x['temperature']) > 12, cities)
for i in filter_temp_spain:
    print(i)
print()

# Count the number of unique countries
print("The number of unique countries")
unique_country = aggregate('country', lambda x:len(set(x)), cities)
print(unique_country)
print()
# Print the average temperature for all the cities in Germany
print("The average temperature for all the cities in Germany")
avg_german_temp = aggregate('temperature',lambda x:sum(x)/len(x), filter_germany)
print(avg_german_temp)
print()
# Print the max temperature for all the cities in Italy
print("The max temperature for all the cities in Italy")
max_italy_temp = aggregate('temperature',lambda x:max(x), filter(lambda x:x['country'] == 'Italy', cities))
print(max_italy_temp)
print()