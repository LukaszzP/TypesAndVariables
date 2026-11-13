###
# Checks whether vehicle speed is within valid range (40-140)
#
speed = int(input('Enter vehicle speed: '))
valid = 40 <= speed <= 140
print('Speed is valid: ', valid)
