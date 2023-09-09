# w.a.p for addition of matrices

r,c=[int(x) for x in input('enter dimensions:  ').split()]
m1=[]
print('Input of Matrix 1')
for i in range (r):
    row=[int(x) for x in input(f'row-{i+1}   ').split()]
    m1.append(row)

m2=[]
print('Input of Matrix 2')
for i in range (r):
    row=[int(x) for x in input(f'row-{i+1}').split()]
    m2.append(row)

m3=[]
for i in range (r):
    row=[]
    for j in range (c):
        row.append(m1[i][j]+m2[i][j])
    m3.append(row)
print(m3)