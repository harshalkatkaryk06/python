# w.a.p to check if the two lists are circularly identical or not
a = eval(input('enter list 1 in []   '))
b = eval(input('enter list 2 in []   '))
a = [str(x) for x in a ]
a = ''.join(a)
b = [str(x) for x in b ]
b = ''.join(b)
if b in a*2:
    print('lists are circularly identical')
else:
    print('lists are not circularly identical')