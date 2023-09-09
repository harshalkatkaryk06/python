# implementations of stack by using list LIFO meathod
stack = []
while True:
    print('-'*30)
    print('1. PUSH\
          \n2.POP\
          \n3.Display\
          \n0.Exit')
    choice = int(input('enter choice:  '))

    if choice==0:
        print('Good Bye')
        break

    elif choice==1:
        item=int(input('enter a number  '))
        stack.append(item)
        print(f'{item} is pushed on to the stack')

    elif choice==2:
        if not stack:
            print('stack is empty')
            continue
        item=stack.pop()
        print(f'{item} is popped')

    elif choice == 3:
        if not stack:
            print('stack is empty')
            continue
        print('stack is: ')
        for x in stack:
            print(x)
    else:
        print('Invalid choice')
    print('-'*30)