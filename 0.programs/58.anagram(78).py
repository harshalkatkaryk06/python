# check if two string are anagrams or not
# if two string contain same numbers of times than two stings are anagrams

s1 = input('enter string 1')
s2 = input('enter string 2')
if sorted(s1)==sorted(s2):
    print(f'{s1} is anagram')
else:
    print(f'{s2} is not anagram')