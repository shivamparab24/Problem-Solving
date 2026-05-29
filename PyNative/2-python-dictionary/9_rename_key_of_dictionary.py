# Write a Python program to rename an existing key in a dictionary while preserving its associated value and the rest of the dictionary unchanged.

employee = {"fname": "John", "age": 30, "dept": "Engineering"}

employee["first_name"] = employee.pop("fname")
print(employee)
print()



def rename_key(d, old_key, new_key):

    if old_key in d:
        d[new_key] = d.pop(old_key)
    else:
        print("Key not found")


if __name__ == "__main__":

    employee = {"fname": "John", "age": 30, "dept": "Engineering"}
    print("Before:", employee)

    old_key = input("Enter key to rename: ")
    new_key = input("Enter new key name: ")

    rename_key(employee, old_key, new_key)
    print("After:", employee)