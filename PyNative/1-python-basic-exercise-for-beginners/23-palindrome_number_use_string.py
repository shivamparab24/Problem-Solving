# Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

def is_palindrome_string_num(number):

    str_num = str(number)
    reverse_str = str_num[::-1]

    if reverse_str == str_num:
        return True
    else:
        return False
    
if __name__ == '__main__':
    n = int(input("enter the number to chekc palindrome: "))
    print(is_palindrome_string_num(n))