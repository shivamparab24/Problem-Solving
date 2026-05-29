# Write a Python program to create a new dictionary containing only the key-value pairs from an existing dictionary where the value meets a specified condition.

scores = {"Alice": 82, "Bob": 45, "Carol": 91, "Dave": 58, "Eve": 73}
print(scores)

new = {}

for k, v in scores.items():
    if v > 60:
        new[k] = v
    
print(new)