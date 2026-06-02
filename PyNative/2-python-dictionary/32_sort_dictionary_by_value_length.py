# Write a Python program to sort a dictionary’s items by the length of their string values, from shortest to longest.

words = {"a": "banana", "b": "kiwi", "c": "strawberry", "d": "fig"}

sorted_words = dict(sorted(words.items(), key=lambda item: len(item[1])))
print(sorted_words)




def value_length(item):
    return len(item[1])

sorted_items = sorted(words.items(), key=value_length)

print(dict(sorted_items))