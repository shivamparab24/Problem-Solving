# Write a program that calculates the factorial of a given number (e.g., 5!) using a for loop.

def factorial(n):

    fact = 1 # 0! = 1

    for i in range(1, n+1): # use inclusive range
        fact = fact * i
        print(fact)
    
    return fact


if __name__ == '__main__':
    
    n = int(input("Enter the number of which you want a factorial: "))
    print("The the factorial is : ", factorial(n))