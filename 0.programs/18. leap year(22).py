# w.a.p to read a year and if it is a leap year or not
year = int(input ('enter a year'))
if year%4==0 and year%100!=0 or year%400==0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')
