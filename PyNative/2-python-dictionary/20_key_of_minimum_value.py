#  Write a Python program to find the key associated with the smallest numerical value in a dictionary.

stock = {"apples": 34, "bananas": 12, "oranges": 57, "grapes": 8, "mangoes": 23}
print(stock)

lowest = min(stock, key = stock.get)
print("Lowest stock item:", lowest)



lowest_key = None
lowest_value = float("inf") #infinity

for key, value in stock.items():    
    if value < lowest_value:
        lowest_value = value
        lowest_key = key

print(lowest_key)