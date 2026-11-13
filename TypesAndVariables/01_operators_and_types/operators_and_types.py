###
# Basic arithmetic, comparison operators, and data types
#
# +  - dodaje wartości
# *  - mnoży wartości
# ** - potęguje wartości
# /  - dzieli i zwraca wartości zmiennoprzecinkowe
# // - dzieli i zwraca wartości całkowite
# %  - modulo zwraca resztę z dzielenia
# >  - sprawdza czy pierwsza wartość jest większa od drugiej i zwraca wartość typu bool
# <= - sprawdza czy pierwsza wartość jest mniejsza lub równa drugiej i zwraca wartość typu bool

print(3 * 2 + 1)            # dwa operatory i trzy argumenty
print(5 + 10 * 5)           # dwa operatory i trzy argumenty
print(4 + 4 / 2 ** 2)       # trzy operatory i cztery argumenty
print(4 % 3 % 2 % 1)        # trzy operatory i cztery argumenty
print(1 + 2 % 3 ** 4 * 5)   # cztery operatory i pięć argumentów
print(True != False)        # jeden operator i dwa argumenty

print(type(50))                                 # zwraca wartość int
print(type(149.17))                             # zwraca wartość float
print(type(4 * 7))                              # zwraca wartość int
print(type(4.0 * 7))                            # zwraca wartość float
print(type("Krakow University of Economics"))   # zwraca wartość string
print(type(True))                               # zwraca wartość bool
print(type(2 > 5))                              # zwraca wartość bool
