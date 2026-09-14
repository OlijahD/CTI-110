# Olijah Dowtin
# September 13, 2026
# P1HW2
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

print("\n------------Travel Expenses------------")
print("Location:", destination)
print(f"Initial Budget: ${budget:.2f}")
print(f"Gas: ${gas:.2f}")
print(f"Accommodation: ${accommodation:.2f}")
print(f"Food: ${food:.2f}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Balance: ${remaining_balance:.2f}")