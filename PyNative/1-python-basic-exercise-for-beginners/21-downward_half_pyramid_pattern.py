# Print a downward half-pyramid pattern using stars (*).
# * * * * * 
# * * * * 
# * * * 
# * * 
# *

n = 100
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
