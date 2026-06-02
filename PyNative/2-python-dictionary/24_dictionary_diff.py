# Write a Python program to find all keys that exist in the first dictionary but are absent from the second dictionary.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"b": 20, "d": 40}

# common = d1.keys() - d2.keys()

common = []

for k1 in d1.keys():
    if k1 not in d2.keys():
        common.append(k1)

print(common)