#max no.
x = eval(input('enter frist number'))
y = eval(input('enter second number'))
if x>y:
    print(f'Maximum = {x}')
else:                                    #alternative print(f'maiimum = {max(x,y)}')
    print(f'Maximum = {y}')