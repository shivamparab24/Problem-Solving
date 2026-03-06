# Write a program to swap the values of two variables, a and b, without using a third temporary variable.

def two_in_place_swap(num1, num2):

    print(f"Before swap the two numbers were {num1} and {num2}")

    num1, num2 = num2, num1

    print(f"After swap the two numbers are {num1} and {num2}")


if __name__ == '__main__':
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    two_in_place_swap(a, b)