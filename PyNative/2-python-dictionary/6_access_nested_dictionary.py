# Write a Python program to retrieve a specific value from a dictionary that is nested inside another dictionary.

person = {"name": "Carol", "address": {"city": "Paris", "zip": "75001"}}


city_1 = person["address"]
print(city_1)

city = person["address"]["city"]
print("City:", city)


city_2 = person.get("address", {}).get("city")
print(city_2)