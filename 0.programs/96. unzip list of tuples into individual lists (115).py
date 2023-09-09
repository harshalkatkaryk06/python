# w.a.p to unzip list of tuples into individual lists

a=eval(input('enter list of tuples ():    '))
out=[]
for t in zip (*a):
    out.append(list(t))
print(out)