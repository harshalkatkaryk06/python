num = int(input('Enter a number: '))
digit = int(input('Enter a digit to count its occurrences: '))
last_digit=digit
occurrences = 0
while num != 0:
    last_digit = num % 10
    if last_digit == digit:
        occurrences += 1
    num = num // 10

print(f'The digit {digit} occurs {occurrences} time(s) in the number.')
