# w.a.p to perform this task: i/p - A2B3C4
                            # o/p - ACBECG
s = input('enter a string: ')
out = ''
for x in s:
    if x.isdigit():
        out=out+chr(ord(out[-1])+int(x))           #ord = order
    else:
        out+=x
print(out)