# w.a.p to read three numbers and find the largest
x = eval(input('enter first number'))
y = eval(input('enter second number '))
z = eval(input('enter third number'))
if x>y and x>z:
    print(f'Largest = {x}')
elif y>z:
    print(f'largest = {y}')
else:
    print(f'largest = {z}')