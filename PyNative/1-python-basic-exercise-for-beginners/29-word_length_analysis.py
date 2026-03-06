# Create a list of 5 words. Write a loop that iterates through the list and prints each word alongside its character count.

def word_length(words):

    for i in words:
        print(f"{i} - {len(i)},", end=" ")

if __name__ == '__main__':
    a = list(map(str, input("Enter the elements of the list: ").split()))
    word_length(a)
