# w.a.p to print Fibonacci series upto given terms
n = int(input('How many terms'))
print('Fibonacci series')
print('0\t1','end\t')          # initial two terms
x=0
y=1

for i in range (n-2):
    z = x+y                           # add two numbers
    print(z,end='\t')
    x = y                             # shift x to y
    y = z                             # shift y to z
