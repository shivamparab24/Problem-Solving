# Write a Python program to organize a list of words into a dictionary where each key is a starting letter and the corresponding value is a list of all words beginning with that letter.

words = ["apple", "avocado", "banana", "blueberry", "cherry", "apricot"]

grouped = {}
for word in words:
    letter = word[0]
    grouped.setdefault(letter, []).append(word)

print(grouped)