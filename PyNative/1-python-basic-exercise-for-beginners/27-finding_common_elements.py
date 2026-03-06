# Take two lists and find the elements that appear in both. Use Sets to perform the operation.


def common_elements(list1, list2):

    set1 = set(list1)
    set2 = set(list2)

    return set1 & set2


if __name__ == '__main__':
    a = list(map(int, input("Enter the first list: ").split()))
    b = list(map(int, input("Enter the second list: ").split()))

    print(common_elements(a, b))