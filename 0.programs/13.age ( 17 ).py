# w.a.p to read a number from user and print child if the age is below 18; adult if the age is 18 or above,
# senior if the age is 65 or above

age = int(input('enter age'))
if age < 18:
    print('child')
elif age < 65:
    print('adult')
elif age < 120:
    print('senior citizen')
else:
    print('invalid age')