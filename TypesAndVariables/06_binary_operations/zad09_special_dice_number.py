###
# Checks whether dice roll result is 1 or 6
#
dice_rolled = int(input('Dice rolled: '))
is_special = dice_rolled == 1 or dice_rolled == 6
print(f'Special number (1 or 6): {is_special}')
