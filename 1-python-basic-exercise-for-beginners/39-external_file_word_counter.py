# Write a script that opens an existing .txt file and counts the total number of words it contains.


with open("notes.txt", "r") as file:
    data = file.read()
    words = data.split()
    word_count = len(words)
    print(f"The file contains {word_count} words.")