# Write a program to check if a given number is a palindrome (reads the same forwards and backwards).

def is_palindrome(number):
    
    temp = number
    reverse = 0

    while temp > 0:
        n = temp % 10
        reverse = reverse * 10 + n
        temp = temp // 10

    if reverse == number:
        return True
    else:
        return False
    

if __name__ == "__main__":
    n = int(input("Enter number to check palindrome: "))
    print(is_palindrome(n))