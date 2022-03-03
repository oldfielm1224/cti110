#CTI-110
#P2HW2 - Score Avg
#Michael Oldfield
#03-02-2022
#
#Program will ask user to input 7 scores.
#Program will store scores in a list.
#Program will determine the lowest score and store in a variable.
#Program will drop the lowest score from the list.
#Calculate score average after dropping lowest score.
#Display lowest score entered, score list with lowest score dropped from the list
#and the average of scores in the modified list.
#
score1 = float(input('\nEnter score #1 '))
score2 = float(input('Enter score #2 '))
score3 = float(input('Enter score #3 '))
score4 = float(input('Enter score #4 '))
score5 = float(input('Enter score #5 '))
score6 = float(input('Enter score #6 '))
score7 = float(input('Enter score #7 '))

scorelist = [score1,score2,score3,score4,score5,score6,score7]
lowestscore = min(scorelist)
scorelist.remove(lowestscore)

print()
print('--------------Results-------------- ')
print('Lowest score  :', min(scorelist))
print('Modified List :', scorelist)
print('Scores Average:', (sum(scorelist) / len(scorelist)))
print('----------------------------------- ')



                                





