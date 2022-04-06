#CTI-110
#P4HW2
#Michael Oldfield
#04-06-2022
#Program will display the number of slices and pizzas depending on the number of
#people.
#Program will require user input for the number of students, and people per whole pizza.
#Program will record if the correct number of people per pizza was entered, and ask the user
#to re-enter correct number.
#Program will ask user if they want to run the program again before it exits.
#

import math

def main():
    valid_people_count = [1.5, 2, 3]
    pizza_cost = 5.00
    students = int(input('How many students do you want to order pizza for?'))
    people_per_pizza = float(input('Enter the number of people per pizza (1.5, 2, or 3):'))
    while people_per_pizza not in valid_people_count:
        print()
        print('INVALID ENTRY!!!!')
        print('Should have entered 1.5, 2, or 3')
        print()
        people_per_pizza = float(input('Enter number of people per pizza again. (1.5, 2, or 3):'))
    pizzas_needed = math.ceil(students / people_per_pizza)
    price = pizzas_needed * (pizza_cost * .06) + (pizzas_needed * pizza_cost)
    print()
    print('Number of Students :', students)
    print('Pizzas Needed :', pizzas_needed)
    print(f'Price ${price:.2f}')

run_again = 'y'
while run_again == 'y':
    main()
    run_again = input('Would you like to run the program again (y for yes):')

                                         
