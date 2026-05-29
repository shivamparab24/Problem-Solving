# Write a Python program to create a dictionary from a list of keys, assigning the same default value to every key.

keys = ["math", "science", "english", "history"]
default = 0

dict1 = {}

for k in keys:
    dict1[k] = default

print(dict1)

# dict1["math"].append(1) #AttributeError: 'int' object has no attribute 'append'
# print(dict1)



# better version of above
dict2 = {}

for k in keys:
    dict2[k] = []
print(dict2)
dict2["math"].append(1)
print(dict2)


# only for immutable default 
scores = dict.fromkeys(keys, default)
print(scores)


keys = ["a", "b", "c"]
d = dict.fromkeys(keys, [])
print(d)    # {'a': [], 'b': [], 'c': []}
d["a"].append(1)
print(d)    # {'a': [1], 'b': [1], 'c': [1]}


# alternative fir above
d = {k: [] for k in keys}
print(d)    # {'a': [], 'b': [], 'c': []}
d["a"].append(1)
print(d)    # {'a': [1], 'b': [], 'c': []}