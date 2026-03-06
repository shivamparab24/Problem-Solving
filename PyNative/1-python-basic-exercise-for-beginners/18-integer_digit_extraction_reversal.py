# Write a program to extract each digit from an integer in the reverse order.

def integer_digit_extraction_reversal(number):

    while number > 0:
        digit = number % 10
        number = number // 10
        print(digit, end=" ")


if __name__ == "__main__":
    n = int(input("Enter the number: "))
    integer_digit_extraction_reversal(n)