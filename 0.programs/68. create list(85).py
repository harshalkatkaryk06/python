# w.a.p to create list of all int from 1 to 10 with and without
# M1 with BIF function
a = list(range(1,11))
print(a)

# M2 without BIF
a = []
for x in range(5,21):
    a.append(x)
print(a)

# M3 by using comprehension
a = [x for x in range (2,12)]
print(a)