# Write a Python program to remove all key-value pairs from a dictionary where the value is None.

data = {"name": "Alice", "age": None, "city": "Paris", "score": None}

clean = {}

for k, v in data.items():
    if v == None:
        clean[k] = data[k]

print(dict(data.items() - clean.items()))