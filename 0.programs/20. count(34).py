# w.a.p to count digits of number

n = int(input('enter a number'))
c=0
while n!=0:
    c+=1
    n=n//10
print(f'sum of digits = {c}')