# CTI-110
# P5HW1 - Score List
# Michael Oldfield
# 04-23-2022
#
#Create a program that will collect scores input by the user.
#Program will give user a menu with multiple options.
#Program will display a score average, a letter grade, and a calculated average.
#Program will determine if a score input is valid.
#The program will determine the lowest score entered.
#A modified list minus the lowest score.
#The average of the scores in the modified list.
#And then determine the letter grade for the average of the scores in the modified list.
#Program will terminate with users choosing the option to exit.

scorelist = []
total = 0

def mainMenu():
    print('-----------MENU-------------')
    print(' 1) Create Score List ')
    print(' 2) Display Results ')
    print(' 3) Exit ' )
    print('----------------------------------')
    print()
    selection = int(input('Enter choice: '))
    if selection == 1:
        create_score_list()
    elif selection == 2:
        if not scorelist:
            print('\nNo Score List has been created.')
            mainMenu()
        else:
            display_results()
    elif selection == 3:
        exit
        print()
        print('Program terminating....')
        print('Good Bye!')
    else:
        print(' \nINVALID choice entered !!!!! \nChoose from menu options please ')
        mainMenu()

def create_score_list():


    number_of_scores = int(input(' \nHow many scores do you want to enter?'))
    
    print('\n')
    for scores in range(number_of_scores):
        score_invalid = True
        while score_invalid:
            user_input_score = int(input(f'Enter score # {scores + 1}: '))
            if (0 <= user_input_score <=100):
                score_invalid = False
            else:   
                score_invalid = True
            if score_invalid:
                print(' \nINVALID Score entered!!!! \nScore should be between 0 and 100 ')
            else:
                scorelist.append(user_input_score)
    mainMenu()    

def display_results():
    lowestscore = min(scorelist)
    scorelist.remove(lowestscore)
    averageScore = (sum(scorelist) / len(scorelist))

    print()
    print('--------------Results-------------- ')
    print('Lowest score  :', lowestscore)
    print('Modified List :', scorelist)
    print('Scores Average:', averageScore)
    if averageScore < 60:
        print('Grade          : F')
    elif averageScore < 70:
        print('Grade          : D')
    elif averageScore < 80:
        print('Grade          : C')
    elif averageScore < 90:
        print('Grade          : B')
    else:
        print('Grade          : A')
        print('----------------------------------- ')
        print()
    mainMenu()
    
mainMenu()
