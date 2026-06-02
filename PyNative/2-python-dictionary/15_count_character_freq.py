# Write a Python program to count how many times each character appears in a given string, storing the results in a dictionary.


text = "hello world"

freq = {}

for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)




freq1 = {}
for char in text:
    freq1[char] = freq1.get(char, 0) + 1

print(freq1)
