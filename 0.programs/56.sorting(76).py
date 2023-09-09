# sort elements of string letter wise and word wise
# letter wise sorting
s = input('enter a string ')
a = sorted(s)
out = ' '.join(a)
print(out)

# letter wise sorting
s = input('enter a string ')
a = s.split()
a = sorted(a)
out = ' '.join(a)
print(out)
