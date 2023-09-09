import numpy as np

print('Enter 10 integers separated by spaces:', end=' ')
a = [int(x) for x in input().split()]

a = np.array(a)

n = int(input('Enter a number: '))
a = a * n

print(a)
