a = input('enter list in []  ').split()
c = 0
for s in a:
    if len(s) >= 2 and s[0] == s[-1]:
        c += 1
print(c)
