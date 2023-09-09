# w.a.p to read a mobile number and check if it can be a valid number

mob = input('enter a number')
if len(mob) == 10 and mob.isdigit():
    print(f'{mob} can be valid')
else:
    print(f'{mob} is not valid')
