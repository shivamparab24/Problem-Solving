# Write a program that takes two separate dictionaries and merges them into one single dictionary.

def merge_dict1(dict1, dict2):
    return dict1 | dict2

def merge_dict2(dict1, dict2):
    dict1.update(dict2) #merges the dicts
    return dict1




def input_dict(dict_name):
    d = {}

    num_entries = int(input(f"Enter the number of entries for {dict_name}: "))

    for _ in range(num_entries):
        key = input("Enter a key: ")
        value = input("Enter a value: ")
        d[key] = value

    return d

if __name__ == '__main__':
    # dict1 = list(map(int, input("Enter the first dictionary: ")))
    # dict2 = list(map(int, input("Enter the second dictionary: ")))


    # dict1 = {}

    # num_entries = int(input("Enter the number of entries for dict1: "))

    # for _ in range(num_entries):
    #     key = input("Enter a key: ")
    #     value = input("Enter a value: ")
    #     dict1[key] = value #

    # print(dict1)


    # dict2 = {}

    # num_entries = int(input("Enter the number of entries for dict2: "))

    # for _ in range(num_entries):
    #     key = input("Enter a key: ")
    #     value = input("Enter a value: ")
    #     dict2[key] = value #

    # print(dict2)
    
    dict1 = input_dict("dict1")
    print(dict1)

    dict2 = input_dict("dict2")
    print(dict2)

    # dict1 = {"name": "Alice", "age": 25}
    # dict2 = {"city": "New York", "job": "Engineer"}

    print(f"the final merged dictionary is: {merge_dict1(dict1, dict2)}")
    print(f"the final merged dictionary is: {merge_dict2(dict1, dict2)}")
    # print(merge_dict1(dict1, dict2))