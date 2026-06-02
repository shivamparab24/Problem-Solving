# Write a Python program to count the frequency of each word in a string, treating words case-insensitively so that “The” and “the” are counted as the same word.

text = "the cat sat on the mat the cat"

word_count = {}

for s in text.lower().split():
    if s not in word_count.keys():
        word_count[s] = 1
    else:
        word_count[s] += 1

print(word_count)