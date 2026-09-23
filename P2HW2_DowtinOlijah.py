# Olijah Dowtin
# September 23, 2026
# P2HW2
# This program stores six module test grades and displays grade statistics.

# Pseudocode:
# Ask for each of the six module test grades
# Store the grades in a list
# Find the lowest and highest grades
# Calculate the sum and average
# Display the results with the average to two decimal places

module_1 = float(input("Enter grade for Module 1: "))
module_2 = float(input("Enter grade for Module 2: "))
module_3 = float(input("Enter grade for Module 3: "))
module_4 = float(input("Enter grade for Module 4: "))
module_5 = float(input("Enter grade for Module 5: "))
module_6 = float(input("Enter grade for Module 6: "))

module_grades = [module_1, module_2, module_3, module_4, module_5, module_6]
lowest_grade = min(module_grades)
highest_grade = max(module_grades)
sum_of_grades = sum(module_grades)
average_grade = sum_of_grades / len(module_grades)

print("\n-------------Results-------------")
print(f'{"Lowest Grade:":<22}{lowest_grade}')
print(f'{"Highest Grade:":<22}{highest_grade}')
print(f'{"Sum of Grades:":<22}{sum_of_grades}')
print(f'{"Average:":<22}{average_grade:.2f}')
print("---------------------------------------------")