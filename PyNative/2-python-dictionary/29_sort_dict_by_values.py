# Write a Python program to sort a dictionary’s items based on their values in ascending order.

scores = {"Alice": 88, "Bob": 72, "Charlie": 95, "Diana": 60}

data = sorted(scores.values())
print(data)


sorted_keys = sorted(scores, key=scores.get)
print(sorted_keys)

# main
sorted_scores = dict(sorted(scores.items(), key=lambda item: item[1]))
print(sorted_scores)