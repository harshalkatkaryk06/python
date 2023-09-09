#ternary or conditional operator
#syntax...   statement.1   if condition   else  statement.2
# even odd prog.
n=eval(input('enter a number'))
print(f'{n} is even')  if n%2==0 else print(f'{n} is odd')

#find minimum
x = eval(input('enter frist number'))
y = eval(input('enter second number'))
m = x  if x<y else y
print(f'minimum = {m}')