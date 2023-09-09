print('enter 10 integrers',end='')
a = [int(x) for x in input().split()]
n = int(input('enter the number  '))
for i in range (len(a)):
    a[i] = a[i]*n
print(a)