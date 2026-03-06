# Iterate through a given list of numbers and print only those numbers which are divisible by 5.



# def filter_condition(a):

#     for i in a:
#         if i % 5 == 0:
#             print(i)

# if __name__ == '__main__':
#     alist = list(map(int, input("Enter the elements: ").split()))
#     filter_condition(alist)



def filter_condition(a):
    
    b = []
    for i in a:
        if i % 5 == 0:
            b.append(i)

    return b

if __name__ == '__main__':
    alist = list(map(int, input("Enter the elements: ").split()))
    print(filter_condition(alist))
