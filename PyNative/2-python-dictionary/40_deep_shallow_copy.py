# Write a Python program that demonstrates the difference between a shallow copy and a deep copy of a dictionary containing nested lists, showing how changes to nested data affect each copy differently.

original = {"name": "Alice", "scores": [90, 85, 92]}

# Shallow copy
shallow = original.copy()
shallow["scores"].append(100)
print("Shallow copy scores:", shallow["scores"])
print("Original scores after shallow mutation:", original["scores"])

print()

# Restore original for a clean deep copy demo
original = {"name": "Alice", "scores": [90, 85, 92, 100]}

import copy
# Deep copy
deep = copy.deepcopy(original)
deep["scores"].append(99)
print("Deep copy scores:", deep["scores"])
print("Original scores after deep mutation:", original["scores"])