#w.a.p to print
#
#       1
#     1 2 1
#   1 2 3 2 1
# 1 2 3 4 3 2 1

for i in range(1,5):
    for j in range(5,i,-1):
        print(' ',end='')
    for j in range(1,i+1):
        print(j,end='')
    for j in range(i-1,0,-1):
        print(j,end='')
    print()
    # optional

   # n = 1
   # for i in range(1, 5):
     #   print(f'{n ** 2 :^10}')
    #    n = n * 10 + 1



