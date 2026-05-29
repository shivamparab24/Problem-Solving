# Write a Python program to verify whether a specific value is present anywhere in a dictionary.

roles = {"alice": "admin", "bob": "editor", "carol": "viewer"}
print(roles)

check = ["editor", "manager"]

for k in check:
    if k in roles.values():
        print(f"{k} exists...")
    else:
        print(f"{k} does not exists...")

