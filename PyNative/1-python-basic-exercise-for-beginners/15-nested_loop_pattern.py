# Print the following pattern where each row contains a number repeated a specific number of times based on its value

# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5




n = int(input("Enter the vale of pattern: ")) #5 since range is n+1

for i in range(n + 1):
    for j in range(i):
        print(i, end=" ")
    print()
