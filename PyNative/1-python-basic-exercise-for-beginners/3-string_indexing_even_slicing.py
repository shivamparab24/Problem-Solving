# Display only those characters which are present at an even index number in given string.

def string_indexing_even_slicing(s):

    # [start = 0, stop = len(s) - 1, and step = 2]
    even_chars = s[0::2]

    print("Printing only even index")
    for char in even_chars:
        print(char)
    

if __name__ == '__main__':
    s = str(input("Enter the word..."))
    string_indexing_even_slicing(s)