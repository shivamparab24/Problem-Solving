# Write a Python program to create a new dictionary containing only the key-value pairs that are identical in both input dictionaries.

d1 = {"a": 1, "b": 2, "c": 3}
d2 = {"a": 1, "b": 99, "c": 3}



inter = {}

for k, v in d1.items():
    if k in d2 and d2[k] == v:
        inter[k] = v

print(inter)






common_keys = d1.keys() & d2.keys()

result = {}

for k in common_keys:
    if d1[k] == d2[k]:
        result[k] = d1[k]

print(result)