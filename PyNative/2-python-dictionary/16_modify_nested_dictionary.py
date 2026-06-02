# Write a Python program to change a specific value inside a dictionary that is nested within another dictionary.

company = {"name": "TechCorp", "location": {"city": "Berlin", "country": "Germany"}}
print(company)

company['location']['city'] = "Munich"
print(company)





def change_country(d, outer_dict, inner_dict, value):
    d[outer_dict][inner_dict] = value


if __name__ == '__main__':

    company = {}

    # Main dictionary input
    company["name"] = input("Enter company name: ")

    # Nested dictionary input
    city = input("Enter city: ")
    country = input("Enter country: ")

    company["location"] = {
        "city": city,
        "country": country
    }

    print("\nBefore update:")
    print(company)

    # User input for updating nested value
    outer_key = input("\nEnter outer key: ")
    inner_key = input("Enter inner key: ")
    new_value = input("Enter new value: ")

    # Function call
    change_country(company, outer_key, inner_key, new_value)

    print("\nAfter update:")
    print(company)







company = {
    "name": "TechCorp",
    "location": {
        "city": "Berlin",
        "country": "Germany"
    }
}

choice = input("What to change (name/city/country): ")

mapping = {
    "name": ("name", None),
    "city": ("location", "city"),
    "country": ("location", "country")
}

if choice in mapping:

    outer, inner = mapping[choice]

    new_value = input("Enter new value: ")

    if inner:
        company[outer][inner] = new_value
    else:
        company[outer] = new_value

else:
    print("Invalid choice")

print(company)