# create list of all squares of int from 1 to 10
# M1: append
a = []
for x in range(1, 11):
    a.append(x*x)
print(a)

#M2: comprehension
a=[x*x for x in range(1,12)]
print(a)