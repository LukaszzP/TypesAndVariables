###
# Calculates discounted price and reduction amount
#
price = float(input('Enter price: '))
discount = int(input('Enter discount: '))
price_w_discount = price * (1 - (discount / 100))
reduction = price - price_w_discount
print('Price with discount: ', round(price_w_discount, 2))
print('Reduction: ', round(reduction, 2))
