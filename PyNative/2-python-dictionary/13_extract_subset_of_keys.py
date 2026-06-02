# Write a Python program to create a new dictionary containing only a specified subset of keys from an existing dictionary.

user = {"id": 42, "username": "jdoe", "email": "jdoe@example.com", "password": "s3cr3t", "joined": "2021-03-15"}
print(user)

extract = ["id", "username", "email"]

extracted = {}


for k, v in user.items():
    if k in extract:
        extracted[k] = v

print(extracted)


extracted1 = {k: user[k] for k in extract}
print(extracted1)
