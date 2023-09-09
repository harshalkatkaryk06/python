# 41(57) using for loop
s = input('enter a string')
for i in range (len(s)):
    print(f'{i}\t{s[i]}\t{i-len(s)}')