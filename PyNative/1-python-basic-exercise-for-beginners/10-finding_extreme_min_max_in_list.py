# Given a list of integers, find and print both the largest and the smallest numbers

def extremes(a):
    return max(a), min(a)


def extremes2(a):
    largest = smallest = a[0]

    for x in a:
        if x > largest:
            largest = x
        if x < smallest:
            smallest = x

    return largest, smallest



if __name__ == '__main__':
    a = list(map(int, input("Enter the elements: ").split()))

    # alternatives for input
    # a = [int(x) for x in input().split()]

    largest1, smallest1 = extremes(a)
    largest2, smallest2 = extremes2(a)

    print(f"1. Largest is {largest1} and smallest is {smallest1}")
    print(f"2. Largest is {largest2} and smallest is {smallest2}")


