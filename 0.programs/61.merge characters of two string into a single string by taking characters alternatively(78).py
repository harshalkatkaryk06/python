# merge characters of two string into a single string by taking characters alternatively
#s1 = python,s2=java
# o/p = pjyatvhaon

s1 = input('enter a string: ')
s2 = input('enter a string: ')
out=''
i=0
while i<len(s1) and i<len(s2):
    out = out + s1[i] + s2[i]
    i+=1
while i < len(s1):
    out = out + s1[i]
    i += 1

while i < len(s2):
     out = out + s2[i]
     i += 1



print(out)