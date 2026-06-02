# Write a Python program to invert a dictionary where multiple keys may share the same value. Instead of overwriting, group all original keys that map to the same value into a list under that value as the new key.

original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

inverted = {}
for k, v in original.items():
    inverted.setdefault(v, []).append(k)

print(inverted)







from collections import defaultdict

original = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}

inverted = defaultdict(list)

for k, v in original.items():
    inverted[v].append(k)

print(dict(inverted))