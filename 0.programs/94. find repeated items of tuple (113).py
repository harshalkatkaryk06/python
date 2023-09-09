# w.a.p to find repeated items of tuple

a = eval(input('enter tuple ():   '))
out = []
for x in a:
    if a.count(x)>1 and x not in out:
        out.append(x)
print(out)