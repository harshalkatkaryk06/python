# w.a.p to print a specified list after removing the zero, 4th,and 5th (BIF-enumerate)
# M1
a = eval(input('enter list in []  '))
out = []
for i in range (len (a)):
    if i not in [0,4,5]:
        out.append(a[i])
print(out)
#M2
a = eval(input('enter list in []  '))
out = []
for i,x in enumerate(a):
    if i not in [0,4,5]:
        out.append(x)
print(out)