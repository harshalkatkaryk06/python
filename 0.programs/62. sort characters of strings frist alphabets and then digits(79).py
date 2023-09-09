# sort characters of strings frist alphabets and then digits
# eg:- i/p B4A2D3
#      o/p ABC234

s = input('enter a string: ')
alpha=digit=''
for x in s:
    if x.isalpha():
        alpha+=x                      # string of alphabets
    else:
        digit+=x                      # sting of digits
out = sorted(alpha)+sorted(digit)     # list of sorted alphabets + sorted digits
out = ''.join(out)
print(out)