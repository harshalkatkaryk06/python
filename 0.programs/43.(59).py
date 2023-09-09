# read and print string in forward and backward with for loop
s = input('enter a string')
print('forward')
for ch in s:
    print(ch)
print('backward')
for ch in s[::-1]:
    print(ch)
