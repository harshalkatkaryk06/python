# w.ap to delete duplicate characters from given string
s = input('enter a string')
out = ''
for ch in s:
    if ch not in out:
        out = out+ch
print(out)