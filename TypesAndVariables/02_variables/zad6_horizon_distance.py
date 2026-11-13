###
# Calculates distance to the horizon based on observer height
#
import math

height_of_observer = float(input('Enter your height in meters: '))
distance = 3.57 * (math.sqrt(height_of_observer))
print('Distance is: ', distance, 'km')

distance2 = 3.57 * math.sqrt(20)
print('Distance from the hotel windows is: ', distance2, 'km')
