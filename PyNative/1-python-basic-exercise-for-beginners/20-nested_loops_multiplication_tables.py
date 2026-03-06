# Print a multiplication table from 1 to 10 in a formatted grid.


number = list(map(int, input("Enter the value: ").split()))

for i in number:
    print()
    # print('multiplication table of:', i)

    for j in range(1, 11):
        # print(f"{i} x {j} = {i * j}")
        print(i * j, end="\t")