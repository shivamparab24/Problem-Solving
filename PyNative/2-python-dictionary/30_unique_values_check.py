# Write a Python program to check whether all values in a dictionary are distinct (i.e., no two keys share the same value).

data = {"a": 1, "b": 2, "c": 3, "d": 2}

d1 = set(data.values())

if len(data) == len(d1):
    print("true")
else:
    print("false")