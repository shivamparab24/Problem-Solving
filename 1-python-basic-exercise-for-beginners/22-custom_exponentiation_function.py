# Write a function called exponent(base, exp) that returns an integer value of the base raised to the power of the exponent.

def expo(base, exp):
    result = 1
    temp = exp
    
    while temp > 0:
        result = result * base
        temp = temp - 1
    
    return result

if __name__ == '__main__':
    base = int(input("Enter the base: "))
    exp = int(input("Enter the exponent: "))
    print(expo(base, exp))