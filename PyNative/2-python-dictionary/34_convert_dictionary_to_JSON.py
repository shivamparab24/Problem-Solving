# Write a Python program to convert a nested dictionary into a formatted JSON string with readable indentation.

person = {"name": "Alice", "age": 30, "address": {"city": "Mumbai", "pin": "400001"}}

import json

person_json = json.dumps(person, indent=4)
print(person_json)