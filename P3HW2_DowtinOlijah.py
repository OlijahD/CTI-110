# Olijah Dowtin
# October 10, 2026
# P3HW2 - Salary
# Calculate an employee's regular pay, overtime pay, and gross pay.

"""
Pseudocode:
Ask for the employee's name, hours worked, and pay rate.
If hours worked are greater than 40:
    Set regular hours to 40.
    Calculate overtime hours as hours worked minus 40.
    Calculate overtime pay as overtime hours times pay rate times 1.5.
Else:
    Set regular hours to hours worked.
    Set overtime hours and overtime pay to zero.
Calculate regular pay as regular hours times pay rate.
Calculate gross pay as regular pay plus overtime pay.
Display the employee's name and the formatted pay information.
"""

employee_name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

if hours_worked > 40:
    regular_hours = 40
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * 1.5
else:
    regular_hours = hours_worked
    overtime_hours = 0
    overtime_pay = 0

regular_pay = regular_hours * pay_rate
gross_pay = regular_pay + overtime_pay

print()
print("-------------------------------------------------------------------------------")
print("Employee name:", employee_name)
print()
print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'OverTime':<12}{'OverTime Pay':<15}{'RegHour Pay':<15}{'Gross Pay':<12}")
print("-------------------------------------------------------------------------------")
print(f"{hours_worked:<15.2f}{pay_rate:<12.2f}{overtime_hours:<12.2f}{overtime_pay:<15.2f}{regular_pay:<15.2f}{gross_pay:<12.2f}")
