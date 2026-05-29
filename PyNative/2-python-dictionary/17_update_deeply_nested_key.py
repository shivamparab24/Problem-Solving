# Write a Python program to update a value located multiple levels deep inside a nested dictionary structure.

data = {"school": {"department": {"class": {"teacher": "Mr. Smith", "students": 30}}}}
print(data)

data["school"]["department"]["class"]["students"] = 35
print(data)




def update_nested(data, keys, value):
    current = data

    for key in keys[:-1]:
        if key not in current:
            raise KeyError(f"Key '{key}' not found")

        current = current[key]

    current[keys[-1]] = value


print("Before:", data)

update_nested(
    data,
    ["school", "department", "class", "students"],
    35
)

print("After:", data)