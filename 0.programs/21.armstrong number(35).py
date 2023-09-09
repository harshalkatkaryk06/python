# w.a.p to check if given number is armstrong or not
# A armstrong number is if sum of cube of digits is equal to original number
n = int(input('enter a number'))
t = n
s = 0
while n!=0:
    r =n%10
    s =n+r**3
    n =n//10
if s==t:
    print(f'{t} is armstrong')
else:
    print(f'{t} is not armstrong')