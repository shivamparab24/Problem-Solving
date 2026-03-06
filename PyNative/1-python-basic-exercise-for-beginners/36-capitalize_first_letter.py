# Write a program to capitalize the first letter of each word in a given string without using the built-in .title() method.

def cap_first_letter_each_word(text):
    words = text.split()
    capitalized_words = []

    for word in words:
        capitalized_words.append(word.capitalize())

    return " ".join(capitalized_words)


if __name__ == '__main__':
    sen = input("Enter the string: ")
    print(cap_first_letter_each_word(sen))