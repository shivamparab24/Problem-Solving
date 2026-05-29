# Write a Python program to invert a dictionary by swapping its keys and values, so each original value becomes a key and each original key becomes the corresponding value.

original = {"a": 1, "b": 2, "c": 3}

inverted = {}

for k, v in original.items():
    inverted[v] = k

print(inverted)