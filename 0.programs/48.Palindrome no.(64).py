# palindrome or not
# meathod 1: Arithmatic and while loop

t = n = int(input('enter a number'))
rev = 0
while n!=0:
    r=n%10
    rev=rev*10+r
    n=n//10
if rev==t:
    print(f'{t} is palindrome')
else:
    print(f'{t} is not palindrome')
# ========================================================================================================
# ========================================================================================================
a = input('enter a number')   # meathod 2: By converting int into string
b=str(a)
if a==a[::-1]:
    print(f'{a} is palindrome')
else:
    print(f'{a} is not palindrome')