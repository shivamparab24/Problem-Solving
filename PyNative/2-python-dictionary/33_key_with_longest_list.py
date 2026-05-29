# Write a Python program to find the key in a dictionary whose associated list value has the greatest number of elements.

data = {"fruits": ["apple", "banana", "cherry"], "vegs": ["carrot"], "grains": ["rice", "wheat"]}



# longest_key = max(data.items(), key=lambda item: len(item[1]))[0]
# print(longest_key)



largest_key = "" #string dictionary

for key in data:
    if largest_key == "" or len(data[key]) > len(data[largest_key]):
        largest_key = key

print(largest_key)