# w.a.p to perform this task: i/p - a4b3c2
                            # o/p - aaaabbbcc

s = input('enter a string: ')
out = ''
for x in s:
    if x.isdigit():
        out=out+out[-1]*(int(x)-1)
    else:
        out+=x
print(out)