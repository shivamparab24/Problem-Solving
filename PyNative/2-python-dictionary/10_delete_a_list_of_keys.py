# Write a Python program to remove multiple specific keys from a dictionary in one operation.

product = {"id": 101, "name": "Laptop", "price": 999, "stock": 50, "warehouse": "A3"}
print(product)
remove = ["stock", "warehouse"]

for k in remove:
    if k in product:
        product.pop(k)

print(product)