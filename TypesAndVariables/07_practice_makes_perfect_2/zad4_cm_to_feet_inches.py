###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
total_inches = round(cm / 2.54)   # wzrost w calach (zaokrąglony do całości)
feet = total_inches // 12         # pełne stopy
inches = total_inches % 12        # reszta, czyli cale
print(f'I am {cm}cm tall, i.e. {feet} feet and {inches} inches')
