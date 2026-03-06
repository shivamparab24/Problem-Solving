# Ask the user for a sentence. Replace every empty space in that sentence with an underscore (_) and print the final result.

def data_sanitization(text):
    return text.replace(" ", "_")

if __name__ == '__main__':
    a = input("enter the text: ")
    print(data_sanitization(a))