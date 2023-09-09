# w.a.p to calculate sum of following series upto given terms

n = int(input('how many terms'))
y = 1
s = 0
for x in range (1,n+1):
    s=s+x/y
    y*=2
print(s)