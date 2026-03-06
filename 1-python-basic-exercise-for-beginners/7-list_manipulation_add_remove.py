# Create a list of 5 fruits. Add a new fruit to the end of the list, then remove the second fruit (at index 1).


def add_remove(alist, new):

    alist.append(new)
    alist.pop(1)

    return alist

if __name__ == '__main__':

    fruits = input("Enter list of fruits: ").split()
    new_fruit = str(input("Enter the fruit to be added: "))

    print(f"Before : {fruits}")
    add_remove(fruits, new_fruit)
    print(f"After: {fruits}")