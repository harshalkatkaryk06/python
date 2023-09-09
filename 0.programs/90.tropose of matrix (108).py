# w.a.p for tropose of matrix
r,c = [int(x) for x in input('enter dimensions:  ').split()]

a=[]
print('Input of Matrix  ')
for i in range(r):
    row=[int(x) for x in input(f' row-{i+1}').split()]
    a.append(row)

b=[[0 for j in range(r)]for i in range(c)]
for i in range (r):
    for j in range(c):
        b[j][i]=a[i][j]

print(b)