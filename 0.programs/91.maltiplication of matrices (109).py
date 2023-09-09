# w.a.p for multiplication of matrices
import sys
m,n=[int (x) for x in input('Enter dimensions:  ').split()]
p,q=[int (x) for x in input('Enter dimensions:  ').split()]

if n != p:
    print('Matrices cant br multiplied')
    sys.exit(0)

m1=[]
print(f'Enter Matrix 1 ({m}*{n}):   ')
for i in range (m):
    row = [int(x) for x in input().split()]
    m1.append(row)

m2=[]
print(f'Enter Matrix 2 ({p}*{q}):   ')
for i in range (p):
    row = [int(x) for x in input().split()]
    m2.append(row)

m3 = [[0 for j in range(q)]for i in range(m)]
for i in range (m):
    for j in range (q):
        for k in range (n):
            m3[i][j]=m3[i][j]+m1[i][k]*m2[k][j]

print(m3)