# w.a.p to print the numbers of a specified list after removing even numbers from it
a = eval(input('enter a list in []  '))
out = []
for x in a:
    if x%2 != 0:
        out.append(x)
print(out)