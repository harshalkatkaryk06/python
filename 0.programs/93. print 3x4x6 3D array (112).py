# w.a.p to generate 3*4*6 3D array whose each element is *
# M1 = pprint meathod
a = []
for i in range(3):
    m = []
    for j in range(4):
        row = []
        for k in range(6):
            row.append('*')
        m.append(row)
    a.append(m)

# Display the 3D array
for i in range(3):
    for j in range(4):
        for k in range(6):
            print(a[i][j][k], end=' ')
        print()
    print()

# M2 = comprehension pprint meathod
import pprint as pp
a = [[['*' for k  in range (6)]for j in range(4)]for i in range (3)]
pp.pprint(a)