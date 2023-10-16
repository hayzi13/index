a = input(int)
s = ' '
for b in range(len(a)):
    if b % 2 != 0:
        s += a[b]
print(s)
print(len(a))

