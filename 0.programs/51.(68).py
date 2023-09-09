# count occurances of vowel in string

s = input('enter a string')
c = 0
for ch in s:
    if ch in 'aeiouAEIOU':  #also by using [ch.lower()] OR [ch.upper] in 'aeiou':
        c+=1
print(f'number of vowels = {c}')




        