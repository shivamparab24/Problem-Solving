# Write a Python program to calculate the total of all numerical values stored in a dictionary.

expenses = {"rent": 1200, "food": 300, "transport": 150, "utilities": 200}
print(expenses)

sum1 = 0

for v in expenses.values():
    sum1 = sum1 + v

print("Total expenses: ", sum1)


total = sum(expenses.values())
print("Total expenses:", total)