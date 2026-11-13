###
# Converts a decimal number to binary and hexadecimal
#
decimal = int(input('Enter decimal number: '))
number = decimal
result = ''
while number > 0:
    digit = number % 2
    result = str(digit) + result
    number = number // 2
print(f'Binary number: {result}')

digits = '0123456789ABCDEF'
number = decimal
result2 = ''
while number > 0:
    remainder = number % 16
    result2 = digits[remainder] + result2
    number = number // 16
print(f'Hexa number: {result2}')
