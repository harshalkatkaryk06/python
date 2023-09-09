# check if its vowel
# meathod 1 :- By using Logical "OR" Operator

ch = input('enter a character  ')
if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print(f'{ch} is a vowel')
elif ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print(f'{ch} is a vowel')
else:
    print(f'{ch} is not vowel')

# ===========================================================================================================
# ===========================================================================================================
# meathod 2 :- By using membership Operator

ch = input('enter a character  ')
if ch in 'aeiouAEIOU':             #also by using [ch.lower()] OR [ch.upper] in 'aeiou'
    print(f'{ch} is a vowel')
else:
    print(f'{ch} is not vowel')


