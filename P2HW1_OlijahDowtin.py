# Olijah Dowtin
# September 23, 2026
# P2HW1
# This program calculates travel expenses and displays the remaining budget.

# Pseudocode:
# Ask the user to enter their budget
# Ask the user to enter their travel destination
# Ask the user to enter the gas, accommodation, and food expenses
# Add all travel expenses together
# Subtract the total expenses from the budget
# Display the travel information and remaining balance

budget = float(input("Enter your budget: $"))
destination = input("Enter your travel destination: ")
gas = float(input("How much will you spend on gas? $"))
accommodation = float(input("How much will you spend on accommodation? $"))
food = float(input("How much will you spend on food? $"))
total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses

print("\n-----------Travel Expenses-----------")
print(f'{"Location:":<20}{destination}')
print(f'{"Initial Budget:":<20}${budget:.2f}')
print(f'{"Gas:":<20}${gas:.2f}')
print(f'{"Accommodation:":<20}${accommodation:.2f}')
print(f'{"Food:":<20}${food:.2f}')
print(f'{"Total Expenses:":<20}${total_expenses:.2f}')
print(f'{"Remaining Balance:":<20}${remaining_balance:.2f}')