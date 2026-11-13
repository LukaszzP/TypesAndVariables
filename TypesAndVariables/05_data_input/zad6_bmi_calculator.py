###
# BMI Calculator
#
wzrost = float(input("Podaj wzrost w cm: "))
waga = float(input('Podaj wage w kg: '))
bmi = waga / (wzrost / 100) ** 2
bmi = round(bmi, 2)
print('Sprawdz czy twoje bmi jest okej: ', bmi)
