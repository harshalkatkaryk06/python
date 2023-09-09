# menu driven prog.

while True:
    print('\n $$$$MENU$$$$')
    print('1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.Division\n5.POWER\n0.EXIT  ')
    choice =int(input('enter your choice'))

    if choice == 0:
        print('Goodbye!')
        break

    if 1<=choice<=5:
        x=eval(input('enter first  number'))
        y=eval(input('enter second number'))

        if choice==1:
            print(f'Addition={x+y}')
        elif choice==2:
            print(f'Substraction={x-y}')
        elif choice==3:
            print(f'Multiplication={x*y}')
        elif choice==4:
            print(f'Division={x/y}')
        elif choice==5:
            print(f'Power={x**y}')
            print('----------------------------------------------------------------------------------------------')

    else:
        print('Invalid choice')

        print('--------------------------------------------------------------------------------------------------')

