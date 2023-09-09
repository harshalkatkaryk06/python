# w.a.p that takes 2 lists and check if they have at least one common number
a = eval(input('enter list 1 in [] '))
b = eval(input('enter list 2 in []  '))
for x in a:
    if x in b:
        print('there is a common element')
        break
    else:
        print('there is no common element')