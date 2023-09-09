# w.a.p to print it forward and backward with index

s = input('enter a string')
print('forward')
i=0
while i<len(s):
    print(f'{i}\t {s[i]}\t {i-len(s)}')
    i+=1

print('backward')
i=len(s)-1
while i>=0:
    print(f'{i}\t {s[i]}\t {i-len(s)}')
    i-=1