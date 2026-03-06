# Write a program that takes a string and reverses it (e.g., “Python” becomes “nohtyP”).

def string_reversal(text):

    # python slicing notation [start:stop:step]
    reversed_text = text[::-1] # start stop step
    print(reversed_text)


if __name__ == '__main__':
    s = str(input("Enter the word: "))
    string_reversal(s)