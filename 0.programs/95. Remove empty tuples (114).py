# w.a.p to remove empty tuple(s) from list of tuples

#M1:
a = eval(input('enter lists of tuples ():   '))
out = []
for t in a:
    if t:
        out.append(t)
print(out)

#M2:
a = eval(input('enter lists of tuples ():   '))
out = []
while () in a:
    a.remove(())
print(a)