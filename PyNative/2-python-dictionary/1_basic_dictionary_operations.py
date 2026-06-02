#Write a Python program to add a new key-value pair to a dictionary, modify an existing value, and access a specific key.


student = {"name": "Alice", "age": 20, "grade": "B"}
print(student)
student["city"] = "New York"
student['age'] = 23

print(student)



def set_value(d, key, value):
    d[key] = value

def print_dictionary(d):
    print(d)

if __name__ == "__main__":

    emps = {}

    n = int(input("Enter the number of key-value pairs: "))

    for i in range(n):
        key = input("Enter the key: ")
        value = input(f"Enter the value for '{key}': ")
        set_value(emps, key, value)

    print("Dictioanry after input...")
    print(emps)

    update_key = input("Enter the key to update or add: ")
    update_value = input(f"Enter the value for '{update_key}': ")
    set_value(emps, update_key, update_value)

    print("The new dictioanry is...")
    print(emps)




# def add_pair(d):
#     key = input("Enter a new key to add: ")
#     value = input(f"Enter the value for '{key}': ")

#     d[key] = value

#     print("\nDictionary after adding new key-value pair:")
#     print(d)


# def modify_value(d):
#     key = input("\nEnter the key whose value you want to modify: ")

#     if key in d:
#         new_value = input(f"Enter the new value for '{key}': ")
#         d[key] = new_value

#         print("\nDictionary after modification:")
#         print(d)
#     else:
#         print("Key not found!")


# def access_key(d):
#     key = input("\nEnter the key you want to access: ")

#     if key in d:
#         print(f"Value for '{key}': {d[key]}")
#     else:
#         print("Key not found!")


# if __name__ == '__main__':

#     d = {}

#     n = int(input("Enter the number of key-value pairs: "))

#     for i in range(n):
#         key = input(f"Enter key {i+1}: ")
#         value = input(f"Enter the value for '{key}': ")

#         d[key] = value

#     print("\nOriginal Dictionary:")
#     print(d)

#     print("\nChoose an operation:")
#     print("1. Add new key-value pair")
#     print("2. Modify existing value")
#     print("3. Access a key")

#     choice = int(input("\nEnter your choice: "))

#     if choice == 1:
#         add_pair(d)

#     elif choice == 2:
#         modify_value(d)

#     elif choice == 3:
#         access_key(d)

#     else:
#         print("Invalid choice!")