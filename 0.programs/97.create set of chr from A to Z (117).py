# w.a.p to create set of chr from A to Z

#M1: without comp.
a = set()
for x in range(ord('A'),ord ('Z')+1): #ASCII code of A = 65, Z=90
    a.add(chr(x))
print (a)

#M2: with comp.
a={chr(x)for x in range(ord('A'),ord('Z')+1)}
print(a)

#M3: string module:
import string
a=set(string.ascii_uppercase)
print(a)