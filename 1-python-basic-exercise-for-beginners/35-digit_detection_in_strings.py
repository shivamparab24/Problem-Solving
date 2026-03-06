# Write a program to check if a user-entered string contains any numeric digits. Use a for loop to examine each character.


def digit_in_string(text):
    digits = []
    for char in text:
        if char.isdigit():
            digits.append(char)

    return digits


def unique_digits_in_string(text):
    digits = set()

    for char in text:
        if char.isdigit():
            digits.add(char)

    return digits


if __name__ == '__main__':
    sent = input("Enter the text: ")
    digits = digit_in_string(sent)
    digits2 = unique_digits_in_string(sent)
    
    if digits:
        print("Digits found:", digits)
    else:
        print("No digits found")

    if digits2:
        print("Digits found:", digits2)
    else:
        print("No digits found")