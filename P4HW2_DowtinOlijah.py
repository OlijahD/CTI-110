# Olijah Dowtin
# October 27, 2026
# P4HW2
# This program calculates pay for multiple employees and displays pay totals.

# Pseudocode:
# Set the total overtime pay, regular pay, gross pay, and employee count to 0.
# Ask the user to enter an employee name or Done to finish.
# While the employee name is not exactly Done:
#     Ask for the employee's pay rate and hours worked.
#     If the employee worked more than 40 hours:
#         Calculate overtime hours and overtime pay at 1.5 times the pay rate.
#         Calculate regular pay for 40 hours.
#     Otherwise, calculate regular pay for all hours and set overtime pay to 0.
#     Add regular pay and overtime pay to calculate gross pay.
#     Display the employee's pay information.
#     Add the employee's pay to the corresponding totals and add 1 to the count.
#     Ask for the next employee name or Done to finish.
# Display the employee count and the totals for overtime, regular, and gross pay.

total_overtime = 0
total_regular = 0
total_gross = 0
employee_count = 0

employee_name = input('Enter employee name or "Done" to terminate: ')

while employee_name != "Done":
    pay_rate = float(input('How much does the employee get paid per hour? '))
    hours_worked = float(input('How many hours did the employee work? '))

    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * pay_rate * 1.5
        regular_pay = 40 * pay_rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours_worked * pay_rate

    gross_pay = regular_pay + overtime_pay

    print('\n----------------------------------------')
    print('Employee name:', employee_name)
    print()
    print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
    print('--------------------------------------------------------------------------------')
    print(f'{hours_worked:<15.1f}{pay_rate:<11.2f}{overtime_hours:<11.1f}${overtime_pay:<14.2f}${regular_pay:<13.2f}${gross_pay:.2f}')
    print()

    total_overtime = total_overtime + overtime_pay
    total_regular = total_regular + regular_pay
    total_gross = total_gross + gross_pay
    employee_count = employee_count + 1

    employee_name = input('Enter employee name or "Done" to terminate: ')

print('\nTotal number of employees entered:', employee_count)
print(f'Total amount paid for overtime: ${total_overtime:.2f}')
print(f'Total amount paid for regular hours: ${total_regular:.2f}')
print(f'Total amount paid in gross: ${total_gross:.2f}')
