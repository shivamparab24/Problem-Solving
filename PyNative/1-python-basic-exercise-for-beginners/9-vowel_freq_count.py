# Write a program to count the total number of vowels (a, e, i, o, u) present in a given sentence.

def vowel_count(text):

    vowels = 'aeiou'
    print(text)
    count = 0

    for char in text:
        if char in vowels:
            count = count + 1
            print(char)
  
    print(count)

if __name__ == '__main__':
    text = str(input("Enter the string: "))
    vowel_count(text)