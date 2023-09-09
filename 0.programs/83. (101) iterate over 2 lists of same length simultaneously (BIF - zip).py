# w.a.p to iterate over 2 lists of same length simultaneously (BIF - zip)
a = eval(input('enter list 1  '))
b = eval(input('enter list 2  '))
for i in range (len(a)):     #BIF-zip for x,y in zip(a,b):
    print( a[i] ,b[i])         #print(x,y)
