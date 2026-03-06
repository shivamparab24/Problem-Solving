# Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

def comp_bool(a):

    if a[0] == a[-1]:
        return True
    else:
        return False
    
if __name__ == '__main__':
    a = list(map(int, input("Enter the elements: ").split()))
    print(comp_bool(a)) 