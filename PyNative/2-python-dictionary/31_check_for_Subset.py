# Write a Python program to verify whether one dictionary is a subset of another, meaning all key-value pairs of the smaller dictionary exist in the larger one.

main = {"a": 1, "b": 2, "c": 3, "d": 4}
subset = {"a": 1, "c": 3}

# is_subset = subset.items() <= main.items()
# print(is_subset)


is_subset = True

for k in subset:
    if k not in main or main[k] != subset[k]:
        is_subset = False
        break

print(is_subset)