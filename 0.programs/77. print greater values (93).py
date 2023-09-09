# w.a.p to find all values in a list that are greater than specified value
a = eval(input('enter a list in []   '))
n = eval(input('enter a number'))
out = [x for x in a if x>n]            #comprehension
print(out)