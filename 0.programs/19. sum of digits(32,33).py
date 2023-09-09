# w.a.p to find sum of digits of given number
n=int(input('enter a number'))
s=0
while n!=0:
    r=n%10
    s=s+r
    n=n//10
print(f'sum of digits = {s}')

# w.a.p to find product of digits of given number
n=int(input('enter a number'))
s=1
while n!=0:
    r=n%10
    s=s*r
    n=n//10
print(f'sum of digits = {s}')

