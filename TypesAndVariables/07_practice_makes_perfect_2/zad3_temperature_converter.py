###
# Converts temperature from Celsius to Kelvin and Fahrenheit
#
celsius = float(input('Enter temperature in Celsius: '))  # pobieram stopnie Celsjusza z klawiatury
convert_to_kelvin = celsius + 273.15                     # konwertuję stopnie C na K
convert_to_fahrenheit = (celsius * (9 / 5)) + 32         # konwertuję stopnie C na F
print(f'Temperature in Kelvin: {convert_to_kelvin}')     # wypisuję wynik
print(f'Temperature in Fahrenheit: {convert_to_fahrenheit}')
