# Write a Python program to flatten a multi-level nested dictionary into a single-level dictionary, joining nested keys with a dot separator to form the new keys.

nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}

def flatten_dict(d, parent_key="", sep="."):
    flattened = {}

    for key, value in d.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key

        if isinstance(value, dict):
            flattened.update(flatten_dict(value, new_key, sep))
        else:
            flattened[new_key] = value

    return flattened


result = flatten_dict(nested)
print(result)





result1 = {}

def flatten(d, prefix=""):
    for k, v in d.items():
        if isinstance(v, dict):
            flatten(v, prefix + k + ".")
        else:
            result1[prefix + k] = v

flatten(nested)

print(result1)




nested = {"a": 1, "b": {"c": 2, "d": {"e": 3, "f": 4}}}

flat = {}

for k1, v1 in nested.items():
    if isinstance(v1, dict):
        for k2, v2 in v1.items():
            if isinstance(v2, dict):
                for k3, v3 in v2.items():
                    flat[f"{k1}.{k2}.{k3}"] = v3
            else:
                flat[f"{k1}.{k2}"] = v2
    else:
        flat[k1] = v1

print(flat)