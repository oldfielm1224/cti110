#CTI-110
#P3HW2
#Michael Oldfield
#03-22-2022
#Program will display the number of slices and pizzas depending on the number of
#people.
#
#

def main():
    import math
    
students = int(input('How many students do you want to order pizza for?'))
people_per_pizza = float(input('Enter the number of people per pizza ( 1.5, 2, or 3):'))
pizza_cost = 5.00
pizzas_needed = round(students / people_per_pizza)
price = pizzas_needed * (pizza_cost * .06) + (pizzas_needed * pizza_cost)

if people_per_pizza == 1.5:
    print()
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas_needed)
    print(f'Price ${price:.2f}')
elif people_per_pizza == 2:
    print()
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas_needed)
    print(f'Price ${price:.2f}')
elif people_per_pizza == 3:
    print()
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas_needed)
    print(f'Price ${price:.2f}')
else:
    print()
    print('INVALID ENTRY!!!!')
    print('Should have entered 1.5, 2 or 3')
    print()
    print('Run Program again')

main()
