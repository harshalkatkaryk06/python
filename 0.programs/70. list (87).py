# create list of all int from 100 to 200 that are divisible by n
# M1: append
n=int(input('enter a number '))                     # M2 comprehension
a=[]                                                # a=[x for x in range (100,201) if x%n==0]
for x in range(100,201):
    if x%n==0:
        a.append(x)
print(a)