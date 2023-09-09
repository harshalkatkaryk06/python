# w.a.p to create unit of matrix of given size
#without numpy and comprehension

r,c = [int (x) for x in input('enter dimension  ').split()]
mat=[]

for i in range (r):
    row=[]
    for j in range(c):
        row.append(1)
    mat.append(row)

print('matrix is:  ')

for row in mat:
    for x in row:
        print(x,end='\t')
    print()

#2 level comprehension without numpy
# mat = [[1 for j in range(c)]for i in range(r)]

#using numpy
#r,c=[int(x) for x in input('enter dimension'.split())]
# mat = np.ones((r,c),int)
#print('matrix is:  ')
#print(mat)