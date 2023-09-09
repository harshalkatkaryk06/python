# print index of each occurance of substring of a string
s = input('enter a string')
p = input('enter a substring')
k = -1
while True:
    k = s.find(p,k+1)
    if k==-1:
        break
    print(k,end='\t')
