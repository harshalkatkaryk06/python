# w.a.p to calculate power by using for loop
x = eval(input('enter base'))
y = eval(input('enter power'))
p = 1
for _ in range(y):
    p = p * x
print(f'{x} raise to {y} = {p}')