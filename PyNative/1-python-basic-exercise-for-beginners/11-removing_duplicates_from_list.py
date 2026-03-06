# Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

def dedup(a):

    unique = set(a)

    return list(unique)

if __name__ == '__main__':
    alist = list(map(int, input("Enter the list of dup elements: ").split()))
    print("The list is: ", alist)
    print(f"The deduplicated list: {dedup(alist)}")