# w.a.p to read an integer and if it is single digit number or not.

n = int(input('enter a number'))
if n>-10 and n<10:
    print(f'{n} is a single digit number')
else:
    print(f'{n} is not a single digit number')
