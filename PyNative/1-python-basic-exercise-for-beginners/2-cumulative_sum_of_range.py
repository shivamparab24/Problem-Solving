# Iterate through the first 10 numbers (0–9). In each iteration, print the current number, the previous number, and their sum.

def cumu_sum_range(n):

    prev_num = 0
    
    for num in range(n):
        sum = prev_num + num
        print(f"Current Number {num}, Previous Number {prev_num}, Sum: {sum}")
        prev_num = num


if __name__ == '__main__':
    n = int(input("Enter the range: "))
    print("Cumulative sum of the given range is: ")
    cumu_sum_range(n)