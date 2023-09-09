# implementations of stack by using list FIFO meathod
from collections import deque

queue = deque()

while True:
    print('-' * 30)
    print('1. ENQUEUE\
          \n2. DEQUEUE\
          \n3. Display\
          \n0. Exit')
    choice = int(input('Enter choice:  '))

    if choice == 0:
        print('Good Bye')
        break

    elif choice == 1:
        item = int(input('Enter a number: '))
        queue.append(item)
        print(f'{item} is enqueued into the queue')

    elif choice == 2:
        if not queue:
            print('Queue is empty')
            continue
        item = queue.popleft()  # Dequeue from the left side
        print(f'{item} is dequeued')

    elif choice == 3:
        if not queue:
            print('Queue is empty')
            continue
        print('Queue is:')
        for x in queue[::-1]:
            print(x)
    else:
        print('Invalid choice')
    print('-' * 30)
