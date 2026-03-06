# Write a program to find how many times the substring “Emma” appears in a given string.
# "Emma is good developer. Emma is a writer"

def substring_count(a, suba):
    return a.count(suba)


def count_substring(b, subb):
    count = 0
    n = len(subb)
    m = len(b)

    for i in range(m - n + 1):
        for j in range(n):
            if b[i + j] != subb[j]:
                break
        else:
            count += 1

    return count       

def count_find(s, sub):
    count = 0
    start = 0

    while True:
        pos = s.find(sub, start)
        if pos == -1:
            break

        count += 1
        start = pos + len(sub)

    return count


import re

def count_regex(s, sub):
    return len(re.findall(sub, s))


if __name__ == '__main__':
    s = str(input("Enter the string: "))
    sub = str(input("Enter the substring: "))

    print(substring_count(s, sub))
    print(count_substring(s, sub))
    print(count_find(s, sub))
    print(count_regex(s, sub))