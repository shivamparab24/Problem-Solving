# Write a program to print the first 15 terms of the Fibonacci series. The sequence starts with 0 and 1, and each subsequent number is the sum of the two preceding ones.


def fibonacci(n):
    num1, num2 = 0, 1

    for _ in range(n):
        print(num1, end=" ")
        num1, num2 = num2, num1 + num2


def fibonacci2(n):
    seq = []
    num1, num2 = 0, 1

    for _ in range(n):
        seq.append(num1)
        num1, num2 = num2, num1 + num2

    return seq


def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


if __name__ == '__main__':
    n = int(input("Enter the no. of terms: "))

    fibonacci(n)
    print()
    print(fibonacci2(n))
    print()
    fib_sequence = [fibonacci_recursive(i) for i in range(n)]
    print(fib_sequence)