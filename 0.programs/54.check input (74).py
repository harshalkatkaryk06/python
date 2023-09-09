# check if entered character is uppercase,lowerrcase,digit or special character

ch = input('Enter a character:  ')
if len(ch) == 1:
    if ch.isupper():
        print(f'{ch} is uppercase')
    elif ch.islower():
        print(f'{ch} is lowercase')
    elif ch.isdigit():
        print(f'{ch} is digit')
    else:
        print(f'{ch} is special character')
else:
    print('Invalid input')