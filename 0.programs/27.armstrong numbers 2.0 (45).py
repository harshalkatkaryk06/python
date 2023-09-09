# w.a.p to print all armstrong numbers between 1 to 500

for t in range (1,501):
    n = t
    s=0
    while n!=0:
        r=n%10
        s=s+r*r*r
        n=n//10
    if s==t:
        print(f'{t} is armstrong')