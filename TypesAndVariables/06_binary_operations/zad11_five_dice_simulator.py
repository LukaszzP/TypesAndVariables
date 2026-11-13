###
# Symulator rzucania pięcioma kośćmi
#
import random

print("Symulator rzucania kośćmi")
for i in range(5):  # odpowiada za dopilnowanie, żeby wypisało 5 elementów
    dice_roll = random.randint(1, 6)  # losuje liczby od 1 do 6
    print(dice_roll, end=" ")  # wypisuje wylosowane liczby i daje odstępy między nimi
print()
