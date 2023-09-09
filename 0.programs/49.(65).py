# check if a ch is present in str

s = input('enter a string')
ch = input('enter a character')
if ch in s:
    print(f'{ch} is present in {s}')
else:
    print(f'{ch} is not present in {s}')