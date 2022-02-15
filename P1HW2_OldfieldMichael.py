#Program to calculate the number of pizzas needed.
#02-15-2022
#CTI-110 P1HW2 - Pizza Order
#Michael Oldfield
#
pizzaslices = 6
sliceperstudent = 3
student = int(input('How many students do you want to order pizza for?'))
print()
print('----Pizza Order--------')
print('Number of Students :', student)
print('Number of Slices Needed:', student * sliceperstudent)
print('Pizzas Needed :', student * sliceperstudent / pizzaslices)
print('--------------------------')

