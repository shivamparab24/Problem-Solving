# Write a program that takes a year as input and determines if it is a leap year.

# A year is a leap year if:
    # It is divisible by 4
    # Except years divisible by 100
    # Unless they are divisible by 400

    # divisible by 400  -> leap year
    # divisible by 100  -> not leap year
    # divisible by 4    -> leap year
    # otherwise         -> not leap year



def is_leap_year(year):

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
    
if __name__ == '__main__':

    y = int(input("Enter the year: "))
    print(is_leap_year(y))