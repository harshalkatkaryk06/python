# w.a.p to remove duplicates from the list
a = eval(input('enter list in [] '))
out = []
for x in a:
    if x not in out:
        out.append(x)
print(out)