# w.a.p to get smallest number from a list with and without BIF
# M1 without BIF
a = eval(input('enter number  '))
m = a[0]
for x in a:
    if x<m:
        m=x
print(m)

# M2 with BIF
print(min(eval(input('enter a list[]:  '))))