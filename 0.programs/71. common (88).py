# w.a.p to create common elements from 2 lists
a = eval(input('enter list 1 in []   '))
b = eval(input('enter list 2 in []   '))
out = []         #M2(comprehend)  [x for x in a if x in b ]
for x in a:
    if x in b:
        out.append(x)
print(out)