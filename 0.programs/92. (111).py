# w.a.p to find the length in a list of lists whose sum of elements is highest

a = eval(input('enter nested list []    '))
m = sum(a[0])
out = a[0]
for sublist in a[1:]:
    if sum (sublist)>m:
        m=sum(sublist)
        out=sublist
print(out)