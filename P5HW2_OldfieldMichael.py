# Create a program that will ask a user to choose an option from a menu.
# Program will execute functions that generates number either adding or subtracting
# them and asking the user to enter the correct answer.
# Program will determine if the answer entered is correct, too high, or too low,
# and then ask the user to enter the correct answer again.
# Program will also determine if wrong choices are chosen for the menu options.
#
# 04-24-2022
# CTI-110
# P5HW2 - Math Quiz
# Michael Oldfield
#


import random


def mainMenu():
    print('MAIN MENU')
    print('--------------------')
    print(' 1. Adding Random Numbers ')
    print(' 2. Subtracting Random Numbers ')
    print(' 3. Exit ')
    print()
    selection = int(input('Please choose one of the menu options: '))
    if selection == 1:
        handleRandomAdd()
    elif selection == 2:
        handleRandomSubtract()
    elif selection == 3:
        print()
        print('Thank you for playing..!')
        print('Good Bye!')
        exit
    else:
        print(' \nINVALID choice entered !!!! \nChoose from menu options please ')
        mainMenu()

def handleRandomAdd():
    numTries = 0
    randomNumber1 = random.randint( 1, 999 )
    print(' ', randomNumber1)
    randomNumber2 = random.randint( 1, 999 )
    print('+', randomNumber2)
    answer = randomNumber1 + randomNumber2
    guess = 2147438746
    while not (guess == answer):
        guess = int(input('Enter answer.'))
        if guess < answer:
            print('\nSorry, guess is too low.')
            numTries += 1
        elif guess > answer:
            print('\nSorry, guess is too high.')
            numTries += 1
        else:
            print('\nCongratulations!!!! your answer is correct.')
            print('\nNumber of guesses: ', numTries)
    mainMenu()

def handleRandomSubtract():
    numTries = 0
    randomNumber1 = random.randint( 1, 999 )
    print(' ', randomNumber1)
    randomNumber2 = random.randint( 1, 999 )
    print('-', randomNumber2)
    answer = randomNumber1 - randomNumber2
    guess = 2147438746
    while not (guess == answer):
        guess = int(input('Enter answer.'))
        if guess < answer:
            print('\nSorry, guess is too low.')
            numTries += 1
        elif guess > answer:
            print('\nSorry, guess is too high.')
            numTries += 1
        else:
            print('\nCongratulations!!!! your answer is correct.')
            print('\nNumber of guesses: ', numTries)
    mainMenu()

mainMenu()
      
        
