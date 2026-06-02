# Write a Python program to find the key associated with the highest numerical value in a dictionary.

scores = {"Alice": 88, "Bob": 95, "Carol": 72, "Dave": 95, "Eve": 84}
print(scores)

high_value = 0
high_key = None

for k, v in scores.items():
    if v > high_value:
        high_value = v
        high_key = k
    
print(high_key)