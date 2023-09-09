# remove words begining with vowels from given string
s = input('enter a string ')
out = ''

for word in s.split():
     if word[0].lower() not in 'aeiou':
         out = out + word + ' '
print(out)

