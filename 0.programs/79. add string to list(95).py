# w.a.p to insert a given string at the beginning of all items in a list
# eg:  list: [1,2,3,4]
#       o/p: ['emp1','emp2','emp3','emp4']

a = eval(input('enter list in []  '))
s = input('enter a sting')
out=[]
for x in a:
    out.append(s+str(x))
print(out)