#Write a Python program to remove a specific key from a dictionary, retrieve all key-value pairs, and check whether a given key exists.

car = {"brand": "Toyota", "model": "Camry", "year": 2022, "color": "blue"}
print(car)


# car.pop('brand')

# del car["color"]

for k, v in dict.items(car):
    print(k, " ", v)

# print(car)
# print(car.items())


# print("'model' exists:", "model" in car)
# print("'model' exists:", "brandd" in car)



if 'model' in car:
    car.pop('model')

print(car)