# Write a program to find all prime numbers up to 20, but only print every second (alternate) prime number found.

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
            
    return True


def get_primes(limit):
    primes = []
    
    for num in range(2, limit + 1):
        if is_prime(num):
            primes.append(num)
            
    return primes


def print_alternate(primes):
    print("Alternate prime numbers:")
    
    for i in range(0, len(primes), 2):
        print(primes[i], end=" ")


def prime_combined(limit):
    primes = get_primes(limit)
    print_alternate(primes)


if __name__ == "__main__":
    limit = int(input("Enter the limit: "))
    prime_combined(limit)