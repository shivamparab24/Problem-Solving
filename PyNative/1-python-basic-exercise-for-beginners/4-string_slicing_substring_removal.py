# Write a function to remove characters from a string starting from index 0 up to n and return a new string.

def String_Slicing_Substring_Removal(s, n):

    print('Original string:', s)

    a = list(s)
    print(a)

    res1 = s[n:] #ivam
    res2 = s[n+1:] #vam
    return res1, res2

if __name__ == '__main__':
    word = str(input("Enter the word : ")) #shivam
    val = int(input("Enter the index: ")) #2
    print(String_Slicing_Substring_Removal(word, val))