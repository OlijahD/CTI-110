# Olijah Dowtin
# October 27, 2026
# P4HW1
# This program collects scores, drops the lowest score, and displays
# the average and letter grade of the remaining scores.

# Pseudocode:
# Ask how many scores the user wants to enter (at least two).
# Repeat for each score:
#     Ask for a score and keep asking while it is outside 0 through 100.
#     Add the valid score to the list.
# Find and display the lowest score, then remove it from the list.
# Calculate and display the average of the remaining scores.
# Determine and display the letter grade for the average.

print('P4HW1 - Olijah Dowtin')

number_of_scores = int(input('How many scores do you want to enter? '))
while number_of_scores < 2:
    print('Please enter at least 2 scores so one can be dropped.')
    number_of_scores = int(input('How many scores do you want to enter? '))

score_list = []

for score_number in range(1, number_of_scores + 1):
    score = float(input('Enter score #' + str(score_number) + ': '))
    while score < 0 or score > 100:
        print('INVALID Score entered!!!!')
        print('Score should be between 0 and 100.')
        score = float(input('Enter a valid score: '))
    score_list.append(score)

lowest_score = min(score_list)
score_list.remove(lowest_score)
average = sum(score_list) / len(score_list)

if average >= 90:
    letter_grade = 'A'
elif average >= 80:
    letter_grade = 'B'
elif average >= 70:
    letter_grade = 'C'
elif average >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print('\n------------Results------------')
print('Lowest Score  :', lowest_score)
print('Modified List :', score_list)
print('Scores Average:', format(average, '.2f'))
print('Grade         :', letter_grade)
print('--------------------------------')