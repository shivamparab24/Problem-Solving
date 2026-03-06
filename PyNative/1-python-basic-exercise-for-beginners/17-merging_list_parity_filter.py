# Create a new list from two given lists such that the new list contains odd numbers from the first list and even numbers from the second list.

# Given Input:

# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]


def merge_parity(a, b):

    c = []

    for i in a:
        if i % 2 != 0:
            c.append(i)

    for j in b:
        if j % 2 == 0:
            c.append(j)

    return c

if __name__ == '__main__':
    list1 = list(map(int, input("Enter first list: ").split()))
    list2 = list(map(int, input("Enter second list: ").split()))

    print(f"The merged list is: {merge_parity(list1, list2)}")