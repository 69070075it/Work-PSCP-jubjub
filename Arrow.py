'''Arrow'''
s = input()
n = int(input())
k = len(s)

for j in range(k):
    d = s[j]
    for i in range(n):
        if d == "R":
            spaces = " " * (2 * i)
        else:
            spaces = " " * (n - 1 - i)
        stars = "*" * (n - i)
        print(spaces + stars)
    for i in range(n - 2, -1, -1):
        if d == "R":
            spaces = " " * (2 * i)
        else:
            spaces = " " * (n - 1 - i)
        stars = "*" * (n - i)
        print(spaces + stars)
    if j < len(s) - 1:
        print()
