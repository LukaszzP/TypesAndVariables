###
# Checks whether a tree can be cut down based on its circumference
#
circumference = int(input('Enter tree circumference in cm: '))
can_be_cut = circumference / 3.14 >= 50
print(f'Tree can be cut down: {can_be_cut}')
