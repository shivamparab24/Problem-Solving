# Create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers (e.g., 2: 4, 3: 9).


def squares_dictionary(n):

    sqr_dict = {}

    for i in range(1, n + 1):
        sqr_dict[i] = i * i

    return sqr_dict


if __name__ == '__main__':
    a = int(input("Enter the value: "))
    print(squares_dictionary(a))





    # word = text.split()

    # for i in word:
    #     if i in freq:
    #         freq[i] += 1
    #         print(freq)

    #     else:
    #         freq[i] = 1
    #         print(freq)
    
    # print()
    # print(freq)