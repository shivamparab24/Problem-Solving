# Write a Python program to identify all keys that are present in both of two given dictionaries.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "c": 30, "d": 40}

# common = d1.keys() & d2.keys()

common = []

for k1 in d1.keys():
    if k1 in d2.keys():
        common.append(k1)

print(common)