# Start with a list of 10 numbers. Iterate through them and sort them into two separate lists: one for even numbers and one for odd numbers.


def odd_even_list_split(a):
    
    even = []
    odd = []

    for i in a:
        if i % 2 == 0:
            even.append(i)
        else:
            odd.append(i)

    return even, odd


if __name__ == '__main__':
    alist = list(map(int, input("Enter the elements of the list: ").split()))

    even_list, odd_list = odd_even_list_split(alist)

    print("Even numbers: ", even_list)
    print("Odd numbers: ", odd_list)