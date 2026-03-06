# Write a program that counts how many times each word appears in a given paragraph and stores these counts in a dictionary.


def word_count(text):
    freq = {}
    print(freq)

    word = text.split()

    for i in word:
        if i in freq:
            freq[i] += 1
            print(freq)

        else:
            freq[i] = 1
            print(freq)
    
    print()
    print(freq)


if __name__ == '__main__':
    a = input("Enter the text: ")
    word_count(a)