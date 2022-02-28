#The program requests prices for five purchased items.
#The program is to calculate subtotal, sales tax and overall total.
#02/28/2022
#CTI-110 P2HW1 - Total Purchases
#Michael Oldfield
#
#
#User will input prices of 5 different items.
item1 = float(input('\nEnter the price for item #1 '))
item2 = float(input('Enter the price for item #2 '))
item3 = float(input('Enter the price for item #3 '))
item4 = float(input('Enter the price for item #4 '))
item5 = float(input('Enter the price for item #5 '))
#Program will calculate subtotal of the 5 different items.
subtotal = float(item1 + item2 + item3 + item4 + item5)
#The sales tax is 7%
salestax = .07
#Program will calculate the total sales tax with the subtotal
totalsalestax = subtotal * salestax
#Program will calculate the complete total for the 5 items.
overalltotal = subtotal + totalsalestax
#Program will print results of subtotal, total sales tax, and total.
print()
print('-------Results-------')
print('Subtotal = ', format(subtotal, ',.2f'), sep='', end='')
print('\nSales Tax = ', format(totalsalestax, ',.2f'), sep='', end='')
print('\nTotal = ', format(overalltotal, ',.2f'), sep='', end='')
