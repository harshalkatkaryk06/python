# w.a.p to print multiplication chart from 1 to 10

for i in range(1,11):                     # 10 rows
    for j in range(1,11):                 # 10 columns
        print(i*j,end='\t')
    print()                           # line change
    